import NavbarLink from "./NavbarLink";
import myLogo from "../images/LogoTrama.png"
import { LayoutDashboard, Users, Receipt, Table2 } from 'lucide-react';

const links = [
  { to: "/dashboard", icon: <LayoutDashboard/> , label: "Home"},
  { to: "/dashboard/clientes", icon: <Users/>, label: "Clientes" },
  { to: "/dashboard/orcamentos", icon: <Receipt/>, label: "Orçamentos" },
  { to: "/", icon: <Table2/>, label: "Tabela de preços" },
];

const Navbar = () => {
  return (
    <nav
      className={`grid grid-rows-1 grid-cols-6 w-full gap-4 justify-center items-center px-4 transition-all duration-200 ease-in-out`}
    >
      <div className="flex justify-center items-center col-span-1 col-start-1">
        <img className="h-16" src={myLogo} alt=""/>
      </div>
      <ul className="flex justify-evenly lg:col-span-2 col-start-2 md:col-span-3 gap-4 lg:gap-0 items-center">
        {links.map((link) => (
          <NavbarLink key={link.to} to={link.to} icon={link.icon} label={link.label} />
        ))}
      </ul>
    </nav>
  );
};

export default Navbar;
