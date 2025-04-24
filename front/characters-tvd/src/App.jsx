import { useEffect, useState } from "react";
import axios from "axios";
import BannerImage from "../public/vampire-diaries-season-9.webp";
function App() {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    fetchCharacters();
  }, []);

  const fetchCharacters = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/v1/characters");
      setCharacters(response.data);
    } catch (error) {
      console.error("Erro ao buscar personagens:", error);
    }
  };

  const handleCreate = async () => {
    const name = prompt("Nome do personagem:");
    const description = prompt("Descrição:");
    const image = prompt("URL da imagem:");

    if (name && description && image) {
      try {
        const response = await axios.post("http://127.0.0.1:8000/api/v1/characters", {
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
        console.error("Erro ao criar personagem:", error);
      }
    }
  };

  const handleEdit = async (id) => {
    const character = characters.find((char) => char.id === id);
    const name = prompt("Novo nome:", character.name);
    const description = prompt("Nova descrição:", character.description);
    const image = prompt("Nova imagem:", character.image);

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
        console.error("Erro ao editar personagem:", error);
      }
    }
  };

  const handleDelete = async (id) => {
    if (confirm("Tem certeza que deseja excluir este personagem?")) {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/v1/characters/${id}`);
        setCharacters((prev) => prev.filter((char) => char.id !== id));
      } catch (error) {
        console.error("Erro ao excluir personagem:", error);
      }
    }
  };

  const handleView = async (id) => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/v1/characters/${id}`);
      const char = response.data;
      alert(`Nome: ${char.name}\nDescrição: ${char.description}\nOrigem: ${char.origin}`);
    } catch (error) {
      console.error("Erro ao visualizar personagem:", error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#1e1b2f] text-white">

      {/* Header */}
      <header className="bg-[#2c234d] p-6 shadow-md">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div>
            <h1 className="text-4xl font-bold text-violet-300">The Vampire Diaries</h1>
            <p className="text-sm text-violet-100">Explore os personagens icônicos da série</p>
          </div>
          <button
            onClick={handleCreate}
            className="bg-violet-700 hover:bg-violet-800 text-white font-medium px-4 py-2 rounded-md transition duration-300 shadow-md"
          >
            + Novo Personagem
          </button>
        </div>
      </header>

      {/* Conteúdo Principal */}
      <main className="flex-1 p-8 max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8">
        <section>
          <h2 className="text-2xl font-semibold mb-4 border-b border-violet-400 pb-2 text-violet-200">Sobre a Série</h2>
          <p className="text-gray-300 leading-relaxed">
            "The Vampire Diaries" é uma série que mistura romance, drama e suspense sobrenatural,
            centrada na cidade fictícia de Mystic Falls. Com vampiros, bruxas, lobisomens e outros seres,
            a série conquistou fãs ao redor do mundo com sua narrativa intensa e personagens inesquecíveis.
          </p>
          <h3 className="mt-6 text-xl font-semibold text-violet-300">Destaques dos Personagens:</h3>
          <ul className="list-disc list-inside text-gray-400">
            <li>Vampiros com histórias complexas</li>
            <li>Relações intensas e transformadoras</li>
            <li>Conflitos sobrenaturais entre facções</li>
          </ul>
        </section>

        <section className="flex items-center justify-center">
          <div className="w-full h-96 bg-violet-800/30 border-2 border-violet-900 rounded-xl overflow-hidden">
            <img
              src={BannerImage}
              alt="Banner dos Personagens de The Vampire Diaries"
              className="w-full h-full object-cover"
            />
          </div>
        </section>
      </main>

      {/* Cards de Personagens */}
{/* Cards de Personagens */}
<section className="p-8 max-w-7xl mx-auto">
  <h2 className="text-2xl font-bold mb-4 border-b border-gray-300 pb-2 text-violet-800/">Personagens</h2>
  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
    {characters.map((char) => (
      <div key={char.id} className="bg-white rounded-lg shadow-lg overflow-hidden transform hover:scale-105 transition duration-300 flex flex-col h-[400px] w-[280px]">
        {/* Aumentando o tamanho da imagem */}
        <img src={char.image} alt={char.name} className="w-full h-[240px] object-cover" />
        <div className="p-4 flex-1 flex flex-col justify-between">
          <div>
            <h2 className="text-xl font-semibold text-gray-900 mb-1">{char.name}</h2>
            <p className="text-sm text-gray-500 mb-3">{char.description}</p>
          </div>
          <div className="flex justify-between mt-auto space-x-2">
            {/* Ver botão */}
            <button
              onClick={() => handleView(char.id)}
              className="flex items-center gap-1 bg-purple-300 hover:bg-purple-400 text-white text-xs px-3 py-1 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 transition duration-150"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" className="bi bi-eye" viewBox="0 0 16 16">
                <path d="M8 3C4.686 3 2 6 2 8s2.686 5 6 5 6-3 6-5-2.686-5-6-5zM8 10c-1.657 0-3-1.343-3-3s1.343-3 3-3 3 1.343 3 3-1.343 3-3 3z"/>
              </svg>
              Ver
            </button>
            {/* Editar botão */}
            <button
              onClick={() => handleEdit(char.id)}
              className="flex items-center gap-1 bg-purple-500 hover:bg-purple-400 text-white text-xs px-3 py-1 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600 transition duration-150"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" className="bi bi-pencil" viewBox="0 0 16 16">
                <path d="M12.146 1.146a2 2 0 0 1 2.828 2.828l-9.848 9.848a2 2 0 0 1-1.175.541L1.5 13.854a.5.5 0 0 1-.146-.365L2 11.5V8.5l4.848-.146a2 2 0 0 1 1.175.541l9.848-9.848a2 2 0 0 1 2.828 2.828L12.146 1.146z"/>
              </svg>
              Editar
            </button>
            {/* Excluir botão */}
            <button
              onClick={() => handleDelete(char.id)}
              className="flex items-center gap-1 bg-purple-700 hover:bg-purple-600 text-white text-xs px-3 py-1 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-700 transition duration-150"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" className="bi bi-trash" viewBox="0 0 16 16">
                <path d="M5.5 5.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 .5.5V14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5.5z"/>
                <path d="M11 1.5a.5.5 0 0 1-.5-.5h-5A.5.5 0 0 1 5 1.5V2h6V1.5z"/>
              </svg>
              Excluir
            </button>
          </div>
        </div>
      </div>
    ))}
  </div>
</section>

      {/* Footer */}
      <footer className="bg-[#2c234d] p-4 text-center text-sm text-violet-300 shadow-inner">
        © 2025 The Vampire Diaries API.
      </footer>
    </div>
  );
}

export default App;
