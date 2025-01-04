const express = require("express");
const axios = require("axios"); // To make requests to the Python API

const app = express();
const port = 5000;

// Middleware to parse JSON bodies
app.use(express.json());

// POST endpoint to handle query
app.post("/query", async (req, res) => {
  const userQuery = req.body.query;
  
  if (!userQuery) {
    return res.status(400).json({ error: "Query is required" });
  }

  try {
    // Send the query to the Python API (Flask)
    const responseFromPythonAPI = await axios.post("http://localhost:8888/query", {
      query: userQuery,
    });

    // Return the response from the Python API to the frontend
    res.json({
      answer: responseFromPythonAPI.data.answer,
      score: responseFromPythonAPI.data.score,
    });
  } catch (err) {
    console.error("Error fetching response from Python API:", err);
    res.status(500).json({ error: "Failed to get a response from the Python API" });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
