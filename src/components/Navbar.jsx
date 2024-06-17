import React from 'react';
import { Link } from 'react-router-dom';
import './navbar.css';

export default function Navbar() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0" id="navbar">
            <li className="nav-item">
              <Link className="nav-link active" aria-current="page" to="/">Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/about">About</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" href="/" to="/mission">Mission</Link>
            </li>
            <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="/" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Contact
              </a>
              <ul className="dropdown-menu">
                <li><a className="dropdown-item" href="/">Mobile: 0703863172</a></li>
                <li><a className="dropdown-item" href="/">Email: ImariQa23@gmail.com</a></li>
                <li><hr className="dropdown-divider" /></li>
                <li><a className="dropdown-item" href="/">All social media Platforms: @ImariQaKenya</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
}
