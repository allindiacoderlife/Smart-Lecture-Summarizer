import mongoose from "mongoose";

const flashcardSchema = new mongoose.Schema(
  {
    lectureId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Lecture",
      required: true
    },

    question: {
      type: String,
      required: true
    },

    answer: {
      type: String,
      required: true
    }
  },
  { timestamps: true }
);

export default mongoose.model("Flashcard", flashcardSchema);
