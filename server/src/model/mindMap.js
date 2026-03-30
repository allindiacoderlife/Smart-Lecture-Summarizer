import mongoose from "mongoose";

const mindMapSchema = new mongoose.Schema(
  {
    lectureId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Lecture",
      required: true,
      unique: true
    },

    nodes: [
      {
        type: String
      }
    ],

    edges: [
      {
        from: String,
        to: String
      }
    ]
  },
  { timestamps: true }
);

export default mongoose.model("MindMap", mindMapSchema);
