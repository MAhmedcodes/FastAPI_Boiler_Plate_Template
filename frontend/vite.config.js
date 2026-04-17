import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      "/auth": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/users": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/organizations": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/jobs": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
    },
  },
});
