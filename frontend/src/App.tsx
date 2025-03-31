import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Home from "./pages/Home";
import Clients from "./pages/ListaClientes";
import Budgets from "./pages/ListaOrcamentos";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />}>
          <Route index element={<Home />} /> {/* Default route for /dashboard */}
          <Route path="home" element={<Home />} />
          <Route path="clientes" element={<Clients />} />
          <Route path="orcamentos" element={<Budgets />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
