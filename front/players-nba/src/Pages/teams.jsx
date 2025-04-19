import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { Card } from "react-bootstrap"; 
import { Button } from "react-bootstrap"; 
import { motion } from "framer-motion";
import { FaBasketballBall } from "react-icons/fa";

const NBASelection = () => {
  const [teams, setTeams] = useState([]);
  const [selectedTeam, setSelectedTeam] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8001/api/v1/playersNBA/teams/");
        setTeams(response.data);
      } catch (error) {
        console.error("Error fetching teams:", error);
      }
    };

    fetchTeams();
  }, []);

  const handleTeamSelect = (team) => {
    setSelectedTeam(team);
  };

  const handleNavigateToPlayers = () => {
    if (selectedTeam) {
      navigate(`/players?team_id=${selectedTeam.id}`);
    }
  };

  return (
    <div
      className="w-full h-screen bg-cover bg-center"
      style={{
        backgroundImage: selectedTeam
          ? `url(${selectedTeam.image_arena})`
          : "url('/default-arena.jpg')", 
      }}
    >
      <div className="bg-black bg-opacity-50 w-full h-full flex flex-col items-center justify-center">
        <h1 className="text-4xl font-bold text-white mb-6">Select Your NBA Team</h1>
        <div className="grid grid-cols-3 gap-6 p-4 max-w-6xl">
          {teams.map((team) => (
            <motion.div
              key={team.id}
              whileHover={{ scale: 1.1 }}
              className="cursor-pointer"
              onClick={() => handleTeamSelect(team)}
            >
              <Card
                className={`shadow-lg p-4 transition-all ${
                  selectedTeam?.id === team.id ? "bg-blue-500" : "bg-white"
                }`}
              >
                <Card.Body className="text-center">
                  <Card.Title className="font-bold text-xl">
                    <FaBasketballBall className="mr-2" />
                    {team.name}
                  </Card.Title>
                  <p>{team.city}</p>
                  <p>{team.arena}</p>
                </Card.Body>
              </Card>
            </motion.div>
          ))}
        </div>
        {selectedTeam && (
          <Button
            className="mt-6 bg-green-500 text-white font-bold py-2 px-4 rounded hover:bg-green-700"
            onClick={handleNavigateToPlayers}
          >
            Confirm Selection
          </Button>
        )}
      </div>
    </div>
  );
};

export default NBASelection;
