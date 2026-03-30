import axios from "axios";
import Lecture from "../models/Lecture.js";
import { config } from "../config/app.config.js";

export const processLecture = async (lectureId, filePath) => {
  try {
    const res = await axios.post(config.aiService, {
      filePath,
    });

    const { transcript, summary, flashcards } = res.data;

    await Lecture.findByIdAndUpdate(lectureId, {
      transcript,
      summary,
      status: "completed",
    });
  } catch (err) {
    console.log(err);
  }
};
