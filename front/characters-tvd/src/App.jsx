import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8001/api/v1/characters")
      .then(response => setCharacters(response.data))
      .catch(error => console.error("Erro ao buscar personagens:", error));
  }, []);

  return (
    <div className="min-h-screen flex flex-col bg-gray-900 text-white">
      {/* Header */}
      <header className="bg-purple-800 p-4 text-center text-3xl font-bold shadow-lg">
        The Vampire Diaries - Personagens
      </header>

      {/* Navbar */}
      <nav className="bg-purple-700 p-2 flex justify-center space-x-6 shadow-md">
        <a href="#" className="hover:text-purple-300">Início</a>
        <a href="#" className="hover:text-purple-300">Personagens</a>
        <a href="#" className="hover:text-purple-300">Sobre</a>
        <a href="#" className="hover:text-purple-300">Contato</a>
      </nav>

      {/* Conteúdo */}
      <main className="flex-1 p-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {characters.map((char) => (
          <div key={char.id} className="bg-purple-600 rounded-2xl shadow-lg overflow-hidden transform hover:scale-105 transition duration-300">
            <img src={char.image} alt={char.name} className="w-full h-48 object-cover" />
            <div className="p-4">
              <h2 className="text-xl font-semibold mb-2">{char.name}</h2>
              <p className="text-sm text-gray-100">{char.description}</p>
            </div>
          </div>
        ))}
      </main>

      {/* Footer */}
      <footer className="bg-purple-800 p-4 text-center text-sm">
        © 2025 The Vampire Diaries Fan API. Todos os direitos reservados.
      </footer>
    </div>
  );
}

export default App;