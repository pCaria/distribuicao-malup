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

  if (isLoading)
    return <CircularProgress sx={{ display: "block", margin: "20px auto" }} />;
  if (isError) {
    console.error(error);
    localStorage.removeItem("token");
    navigate("/");
    return null;
  }

  return (
    <div className="flex flex-col h-screen w-screen text-white bg-gray-950">

      {/* Topbar */}
      <div className={`flex bg-gray-950 text-white w-screen min-h-20 border-b border-white/10`}>       
        <Navbar />
      </div>

      {/* Content */}
      <div className="flex flex-grow max-w-[1280px] justify-center p-5 md:p-10 lg:px-14 xl:w-[1280px] xl:m-auto 2xl:px-0 xl:py-14">
        <Outlet />
          
      </div>
      
    </div>
  );
};

export default Dashboard;
