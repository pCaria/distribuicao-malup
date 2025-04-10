const Home = () => {
  return (
    <div className="flex flex-col w-full p-4">
      <h2 className="text-xl font-semibold mb-2">Home</h2>
      <p>Welcome to the Home page!</p>
      <div className="overflow-x-auto">
        <table className="table-auto border-collapse border-4 border-gray-800 mt-10 w-full">
          <thead className="bg-gray-200/10">
            <tr>
              <th className="border border-gray-800 px-4 py-2 text-left">Cliente</th>
              <th className="border border-gray-800 px-4 py-2 text-left">Data Abertura</th>
              <th className="border border-gray-800 px-4 py-2 text-left">Status do Orçamento</th>
              <th className="border border-gray-800 px-4 py-2 text-left">Data Fechamento</th>
            </tr>
          </thead>

          <tbody>
            <tr className="odd:bg-white/20 even:bg-gray-100/40">
              <td className="border border-gray-800 px-4 py-2">Petrobras</td>
              <td className="border border-gray-800 px-4 py-2">26/02/2025</td>
              <td className="border border-gray-800 px-4 py-2">Em Aberto</td>
              <td className="border border-gray-800 px-4 py-2">15/03/2025</td>
            </tr>

            <tr className="odd:bg-white/20 even:bg-gray-100/40">
              <td className="border border-gray-800 px-4 py-2">Petrobras</td>
              <td className="border border-gray-800 px-4 py-2">26/02/2025</td>
              <td className="border border-gray-800 px-4 py-2">Em Aberto</td>
              <td className="border border-gray-800 px-4 py-2">15/03/2025</td>
            </tr>

            <tr className="odd:bg-white/20 even:bg-gray-100/40">
              <td className="border border-gray-800 px-4 py-2">Petrobras</td>
              <td className="border border-gray-800 px-4 py-2">26/02/2025</td>
              <td className="border border-gray-800 px-4 py-2">Em Aberto</td>
              <td className="border border-gray-800 px-4 py-2">15/03/2025</td>
            </tr>

            <tr className="odd:bg-white/20 even:bg-gray-100/40">
              <td className="border border-gray-800 px-4 py-2">Petrobras</td>
              <td className="border border-gray-800 px-4 py-2">26/02/2025</td>
              <td className="border border-gray-800 px-4 py-2">Em Aberto</td>
              <td className="border border-gray-800 px-4 py-2">15/03/2025</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Home;
