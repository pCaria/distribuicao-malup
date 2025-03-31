import { useState } from "react";
import { Outlet, useNavigate } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import Navbar from "../components/Navbar";
import api from "../api";
import { CircularProgress } from "@mui/material";

const fetchUserData = async (): Promise<{ nome: string; email: string }> => {
  const token = localStorage.getItem("token");
  if (!token) throw new Error("Token não encontrado");

  const response = await api.get("/auth/me", {
    headers: { Authorization: `Bearer ${token}` },
  });

  return response.data;
};

const Dashboard = () => {
  const navigate = useNavigate();
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  const {
    data: user,
    isLoading,
    isError,
    error,
  } = useQuery({
    queryKey: ["user"],
    queryFn: fetchUserData,
    retry: 1,
    staleTime: 1000 * 60 * 5,
  });

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  const toggleSidebar = (event: React.MouseEvent<HTMLElement>) => {
    if (event.target === event.currentTarget) {
      setIsSidebarOpen(!isSidebarOpen);
    }
  };

  if (isLoading)
    return <CircularProgress sx={{ display: "block", margin: "20px auto" }} />;
  if (isError) {
    console.error(error);
    localStorage.removeItem("token");
    navigate("/");
    return null;
  }

  return (
    <div className="flex flex-col h-screen text-white bg-gray-950">
      {/* Sidebar */}
      <div
        // onClick={toggleSidebar}
        className={`flex bg-gray-950 text-white w-screen h-16 border-b border-white/10`}
      >
        {/* <div
          className={`flex w-max-screen justify-end ${
            isSidebarOpen ? "h-15 p-4 border-b-2 border-white/40" : "h-full p-2 "
          } transition-all duration-600 ease-in-out`}
        >
          <button
            onClick={toggleSidebar}
            className="text-white h-full focus:outline-none"
          >
            {isSidebarOpen ? "<<" : ">>"}
          </button>
        </div> */}
        <Navbar />
      </div>
      <div className="flex overflow-hidden">
        {/* Header */}
        {/* <div className="bg-gray-950 w-full border-b-2 border-white/40 z-30 relative text-white px-4 py-2">
          <div className="flex h-10 justify-between items-center">
            <h1 className="text-xl font-bold">Dashboard</h1>
            <button
              onClick={handleLogout}
              className="text-white hover:underline"
            >
              Logout
            </button>
          </div>
        </div> */}

        {/* Content */}
        <div className="flex p-6 overflow-y-auto">
          <Outlet />
          {/* <h2 className="text-2xl">Bem-vindo, {user?.nome || "Usuário"}!</h2>
          <p className="text-gray-700">Email: {user?.email}</p> */}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
