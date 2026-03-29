import "dotenv/config";

import express from "express";
import cors from "cors";
import { config } from "./config/app.config.js";
import { errorHandler } from "./middleware/errorHandler.js";
import { asyncHandler } from "./utils/asyncHandler.js";
import apiRoutes from "./routes/index.js";

const app = express();

app.use(cors());
app.use(express.json());
//* ─── Backend Running ────────────────────────────────────────────
app.get(
  "/",
  asyncHandler(async (_req, res) => {
    res.json({
      status: "Backend is running",
    });
  }),
);

//* ─── Health Check ────────────────────────────────────────────
app.get(
  "/api/health",
  asyncHandler(async (_req, res) => {
    res.json({
      status: "Backend is healthy",
      timestamp: new Date().toISOString(),
      uptime: process.uptime(),
      environment: config.nodeEnv,
    });
  }),
);

//* ─── API Routes ───────────────────────────────────────────────
app.use("/api", apiRoutes);

//* ─── Error Handler ────────────────────────────────────────────
app.use(errorHandler);

if (process.env.NODE_ENV !== "production") {
  app.listen(config.port, () => {
    console.log(`Server running on http://localhost:${config.port}`);
  });
}
