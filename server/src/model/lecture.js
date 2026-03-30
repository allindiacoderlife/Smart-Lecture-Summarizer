import mongoose from "mongoose";

const lectureSchema = new mongoose.Schema(
  {
    userId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true
    },

    title: {
      type: String,
      required: true
    },

    fileUrl: {
      type: String,
      required: true
    },

    fileType: {
      type: String,
      enum: ["audio", "video", "pdf", "text"],
      required: true
    },

    transcript: {
      type: String,
      default: ""
    },

    summary: {
      type: String,
      default: ""
    },

    status: {
      type: String,
      enum: ["uploaded", "processing", "completed", "failed"],
      default: "uploaded"
    }
  },
  { timestamps: true }
);

export default mongoose.model("Lecture", lectureSchema);
