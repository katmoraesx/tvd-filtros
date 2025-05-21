import { useEffect, useState } from "react";
import axios from "axios";
import BannerImage from "../public/banner-copy.jpg";

const GROUPS = ["Todos", "Vampiros", "Lobos", "Bruxas", "Caçadores", "Humanos"];

function App() {
  const [characters, setCharacters] = useState([]);
  const [selectedGroup, setSelectedGroup] = useState("Todos");
  useEffect(() => {
    const fetchCharacters = async () => {
      try {
        const url =
          selectedGroup === "Todos"
            ? "http://127.0.0.1:8000/api/v1/characters/"
            : `http://127.0.0.1:8000/api/v1/characters/?group=${selectedGroup}`;
        const response = await axios.get(url);
        setCharacters(response.data);
      } catch (error) {
        console.error("Error searching for characters:", error);
      }
    };
  
    fetchCharacters();
  }, [selectedGroup]);
  

  const handleCreate = async () => {
    const name = prompt("Character name:");
    const description = prompt("Description:");
    const image = prompt("Image URL:");

    if (name && description && image) {
      try {
        const response = await axios.post("http://127.0.0.1:8000/api/v1/characters/", {
          name,
          description,
          image,
          age: 0,
          height: 0,
          role: "",
          origin: ""
        });
        setCharacters((prev) => [...prev, response.data]);
      } catch (error) {
        console.error("Error when creating characters:", error);
      }
    }
  };

  const handleEdit = async (id) => {
    const character = characters.find((char) => char.id === id);
    const name = prompt("New name:", character.name);
    const description = prompt("New description:", character.description);
    const image = prompt("New image:", character.image);

    if (name && description && image) {
      try {
        const response = await axios.put(`http://127.0.0.1:8000/api/v1/characters/${id}`, {
          ...character,
          name,
          description,
          image
        });
        setCharacters((prev) =>
          prev.map((char) => (char.id === id ? response.data : char))
        );
      } catch (error) {
        console.error("Error when editing character:", error);
      }
    }
  };

  const handleDelete = async (id) => {
    if (confirm("Are you sure you want delete this character?")) {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/v1/characters/${id}`);
        setCharacters((prev) => prev.filter((char) => char.id !== id));
      } catch (error) {
        console.error("Error when delete character:", error);
      }
    }
  };

  const handleView = async (id) => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/v1/characters/${id}`);
      const char = response.data;
      alert(`Name: ${char.name}\nDescription: ${char.description}\nOrigin: ${char.origin}`);
    } catch (error) {
      console.error("Error when viewing character:", error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#0d0d0d] text-white">
      <header className="bg-[#1a1a1a] p-6 shadow-md border-b border-red-800">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div>
            <h1 className="text-4xl font-bold text-red-600">The Vampire Diaries</h1>
            <p className="text-sm text-gray-400">Explore the series' iconic characters</p>
          </div>
          <button
            onClick={handleCreate}
            className="bg-red-700 hover:bg-red-800 text-white font-semibold px-5 py-2 rounded-xl shadow-lg transition duration-300"
          >
            + New Character
          </button>
        </div>
      </header>

      <main className="flex-1 p-8 max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8">
        <section>
          <h2 className="text-2xl font-semibold mb-4 border-b border-red-600 pb-2 text-red-400">About the series</h2>
          <p className="text-gray-300 leading-relaxed">
            "The Vampire Diaries" is a series that mixes romance, supernatural drama and suspense,
            centered on the fictional town of Mystic Falls. With vampires, witches, werewolves and other beings,
            the series has won fans around the world with its intense narrative and unforgettable characters.
          </p>
          <h3 className="mt-6 text-xl font-semibold text-red-500">Character Highlights:</h3>
          <ul className="list-disc list-inside text-gray-400">
            <li>Vampires with complex stories</li>
            <li>Intense and transformative relationships</li>
            <li>Supernatural conflicts between factions</li>
          </ul>
        </section>

        <section className="flex items-center justify-center">
          <div className="w-full h-96 bg-red-900/30 border-2 border-red-800 rounded-2xl overflow-hidden">
            <img
              src={BannerImage}
              alt="Banner dos Personagens de The Vampire Diaries"
              className="w-full h-full object-cover"
            />
          </div>
        </section>
      </main>

      {/* 🔍 FILTROS POR GRUPO */}
      <section className="px-8 max-w-7xl mx-auto mb-6">
        <div className="flex flex-wrap gap-4 justify-center sm:justify-start">
          {GROUPS.map((group) => (
            <button
              key={group}
              onClick={() => setSelectedGroup(group)}
              className={`px-4 py-2 rounded-full font-medium text-sm transition-all border 
              ${
                selectedGroup === group
                  ? "bg-red-700 border-red-700 text-white"
                  : "bg-[#1a1a1a] border-red-900 text-red-400 hover:bg-red-800 hover:text-white"
              }`}
            >
              {group}
            </button>
          ))}
        </div>
      </section>

      <section className="p-8 max-w-7xl mx-auto">
        <h2 className="text-2xl font-bold mb-6 border-b border-red-700 pb-2 text-red-400">Characters</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-6">
          {characters.map((char) => (
            <div
              key={char.id}
              className="bg-[#1a1a1a] border border-red-900 rounded-2xl shadow-lg overflow-hidden hover:shadow-red-900 hover:scale-[1.02] transition duration-300 flex flex-col"
            >
              <img
                src={char.image}
                alt={char.name}
                className="w-full h-60 object-cover"
              />
              <div className="p-4 flex-1 flex flex-col justify-between">
                <div>
                  <h2 className="text-lg font-bold text-red-500 mb-2 truncate">{char.name}</h2>
                  <p className="text-sm text-gray-300 line-clamp-3 mb-4">{char.description}</p>
                </div>
                <div className="flex gap-2 mt-auto">
                  <button
                    onClick={() => handleView(char.id)}
                    className="flex-1 bg-[#660000] hover:bg-[#990000] text-white text-sm px-4 py-2 rounded-lg font-medium transition"
                  >
                    View
                  </button>
                  <button
                    onClick={() => handleEdit(char.id)}
                    className="flex-1 bg-[#333333] hover:bg-[#555555] text-white text-sm px-4 py-2 rounded-lg font-medium transition"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() => handleDelete(char.id)}
                    className="flex-1 bg-red-700 hover:bg-red-800 text-white text-sm px-4 py-2 rounded-lg font-medium transition"
                  >
                    Delete
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      <footer className="bg-[#1a1a1a] p-4 text-center text-sm text-red-500 shadow-inner border-t border-red-900">
        © 2025 The Vampire Diaries API.
      </footer>
    </div>
  );
}

export default App;
