import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import { TextField, Button, Container, Typography, Box } from "@mui/material";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate(); // Redireciona o Usuario após o Login.

  const handleLogin = async () => {
    try {
      const response = await api.post("/auth/token", {
        username: email,
        password: password,
      });
      localStorage.setItem("token", response.data.access_token); // Salva o token.
      navigate("/dashboard");
    } catch (error) {
      setError("Usuário ou senha incorretos!");
    }
  };
  return (
    <Container maxWidth="xs">
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          marginTop: 8,
        }}
      >
        <Typography variant="h4">Login</Typography>
        <TextField
          label="Email"
          variant="outlined"
          fullWidth
          margin="normal"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <TextField
          label="Senha"
          type="password"
          variant="outlined"
          fullWidth
          margin="normal"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {error && <Typography color="error">{error}</Typography>}
        <Button
          variant="contained"
          color="primary"
          fullWidth
          sx={{ marginTop: 2 }}
          onClick={handleLogin}
        >
          Entrar
        </Button>
      </Box>
    </Container>
  );
};

export default Login;
