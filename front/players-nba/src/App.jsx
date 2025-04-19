import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import NBASelection from "./Pages/teams";
import NBAPlayers from "./Pages/players";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<NBASelection />} /> 
        <Route path="/players" element={<NBAPlayers />} /> 
      </Routes>
    </Router>
  );
};

export default App;
