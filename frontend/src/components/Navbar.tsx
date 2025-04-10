import NavbarLink from "./NavbarLink";
import myLogo from "../images/LogoTrama.png";
import { LayoutDashboard, Users, Receipt, Table2, Menu, SquareUser, X} from "lucide-react";
import { useState } from "react";

const links = [
  { to: "/dashboard", icon: <LayoutDashboard />, label: "Home" },
  { to: "/dashboard/clientes", icon: <Users />, label: "Clientes" },
  { to: "/dashboard/orcamentos", icon: <Receipt />, label: "Orçamentos" },
  { to: "/", icon: <Table2 />, label: "Tabela de preços" },
];

const toggleDropdown = () => {
  let navigationMenu = document.querySelector('.navigation-menu')
    navigationMenu?.classList.toggle('hidden')
};

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav
      className={`grid grid-cols-auto grid-auto-row min-h-20 w-full justify-normal md:mx-4 lg:pl-15 xl:max-w-[1480px] xl:mx-auto items-center`}
    >
      {/* Logo */}
      <div className="col-start-2 row-start-1 md:col-span-[260px] md:col-start-1 items-center">
        <img className="h-20 place-self-center" src={myLogo} alt="" />
      </div>

      {/* Mobile menu icon */}
      <div className="absolute top-7 right-14 justify-self-center md:hidden focus:outline-none">
        <button onClick={() => setIsOpen(!isOpen)} className="mobile-menu-button">
          {isOpen ? <X size={28}/> : <Menu size={28}/>}
        </button>
      </div>

      {/* Navigation Options */}
      <div
        className={`overflow-hidden transition-all duration-300 ease-in-out col-span-3 row-start-2 
          ${isOpen ? "max-h-[500px] opacity-100" : "max-h-0 opacity-0"}
           md:opacity-100 md:max-h-full md:col-start-2 md:col-span-1 md:row-start-1 md:flex md:pr-[40%] md:space-x-4 md:bg-transparent xl:col-span-2`}
      >
        <ul className="flex flex-col md:flex-row items-center py-2 space-y-4 md:space-y-0 md:space-x-6 md:p-0">
          {links.map((link) => (
            <NavbarLink
              key={link.to}
              to={link.to}
              icon={link.icon}
              label={link.label}
            />
          ))}
        </ul>
      </div>

      {/* User Stuff */}
      <div className="hidden md:flex md:row-start-1 lg:pr-4 xl:pr-14 items-center justify-end">
          <SquareUser/>
      </div>
    </nav>
  );
};

export default Navbar;
