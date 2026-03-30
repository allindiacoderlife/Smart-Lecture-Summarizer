export const config = {
  port: process.env.PORT || 3000,
  nodeEnv: process.env.NODE_ENV || "development",
  aiService: process.env.AI_SERVICE || "http://localhost:8000/process",
  jwtSecret: process.env.JWT_SECRET,
  mongoURI: process.env.MONGO_URI,
};
