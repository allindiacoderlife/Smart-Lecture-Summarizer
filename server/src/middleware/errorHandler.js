export const errorHandler = (err, req, res, next) => {
  console.error("Error in error handling middleware: ", err.message);
  console.error(err.stack);
  const statusCode = err.statusCode || 500;
  res.status(statusCode).json({
    message: "Error from error handling middleware",
    error: err.message || "Internal Server Error",
    ...(process.env.NODE_ENV === "development" ? { stack: err.stack } : {}),
  });
};
