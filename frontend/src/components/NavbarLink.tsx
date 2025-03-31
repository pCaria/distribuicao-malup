import { Link } from "react-router-dom";

type NavbarLinkProps = {
  to: string;
  icon: any;
  label: string;
};

const NavbarLink = ({ to, icon, label }: NavbarLinkProps) => {
  return (
    <li className="grow min-w-max">
      <Link
        to={to}
        className="flex w-full justify-center hover:bg-gray-900 rounded"
      >
        <span className="flex w-max font-bold">{label}</span>
      </Link>
    </li>
  );
};

export default NavbarLink;
