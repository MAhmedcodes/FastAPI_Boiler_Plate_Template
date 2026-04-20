import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout/Layout";
import Home from "./pages/Home";
import LoginRegister from "./pages/LoginRegister";
import OTPVerification from "./pages/OTPVerification";
import Logout from "./pages/Logout";
import Organizations from "./pages/Organizations";
import Jobs from "./pages/Jobs";

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/auth" element={<LoginRegister />} />
          <Route path="/otp" element={<OTPVerification />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/organizations" element={<Organizations />} />
          <Route path="/jobs" element={<Jobs />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
