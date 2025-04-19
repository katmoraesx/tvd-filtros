import React, { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import axios from "axios";
import { Card } from "react-bootstrap"; 
import { motion } from "framer-motion";
import { FaBasketballBall } from "react-icons/fa"; 

const NBAPlayers = () => {
  const [players, setPlayers] = useState([]);
  const [team, setTeam] = useState(null);
  const [searchParams] = useSearchParams();
  const teamId = searchParams.get("team_id");

  useEffect(() => {
    const fetchData = async () => {
      if (teamId) {
        try {
          const playersResponse = await axios.get(
            `http://127.0.0.1:8001/api/v1/playersNBA/players/`,
            { params: { team_id: teamId } }
          );
          setPlayers(playersResponse.data);

          const teamResponse = await axios.get(
            `http://127.0.0.1:8001/api/v1/playersNBA/teams/${teamId}/`
          );
          setTeam(teamResponse.data);
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      }
    };

    fetchData();
  }, [teamId]);

  const positionsMap = {
    PG: "Point Guard",
    SG: "Shooting Guard",
    SF: "Small Forward",
    PF: "Power Forward",
    C: "Center",
  };

  return (
    <div
      className="w-full h-screen bg-cover bg-center"
      style={{
        backgroundImage: team
          ? `url(${team.image_arena})`
          : "url('/default-arena.jpg')", // Replace with a default arena image path
      }}
    >
      <div className="bg-black bg-opacity-50 w-full h-full flex flex-col items-center justify-center">
        <h1 className="text-4xl font-bold text-white mb-6">
          {team ? `${team.name} Players` : "Loading Players..."}
        </h1>
        <div className="grid grid-cols-3 gap-6 p-4 max-w-6xl">
          {players.map((player) => (
            <motion.div
              key={player.id}
              whileHover={{ scale: 1.1 }}
              className="cursor-pointer"
            >
              <Card className="shadow-lg p-4 bg-white transition-all">
                <Card.Body className="text-center">
                  <Card.Title className="font-bold text-xl">
                    <FaBasketballBall className="mr-2" />
                    {player.name}
                  </Card.Title>
                  <img
                    src={player.image}
                    alt={player.name}
                    className="w-32 h-32 mx-auto rounded-full mb-4"
                  />
                  <p>Position: {positionsMap[player.position] || player.position}</p>
                  <p>Age: {player.age}</p>
                  <p>Height: {player.height} cm</p>
                  <p>Country: {player.country}</p>
                </Card.Body>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default NBAPlayers;
