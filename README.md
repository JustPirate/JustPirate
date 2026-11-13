<div align="center">

# Vijaygovind Biju

**Software Engineer** — Systems Programming · Linux · Rust · Flutter · AI

*Building practical software from the kernel up.*

[![Portfolio](https://img.shields.io/badge/Portfolio-vijaygovindbiju.github.io-0B1120?style=flat&logo=githubpages&logoColor=white)](https://vijaygovindbiju.github.io/portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-JustPirate-181717?style=flat&logo=github&logoColor=white)](https://github.com/JustPirate)

</div>

---

## About

I'm a software engineer with a focus on understanding how software works beneath the surface — operating system interfaces, runtime behaviour, system-level APIs, and distributed systems — and applying that deep understanding to build reliable, high-performance products.

My work spans **systems programming**, **Linux internals & Wayland**, **cross-platform application development**, and **local-first AI engineering**.

---

## Focus Areas

| Domain | What I work on |
|---|---|
| **Linux & Systems** | Wayland protocols, D-Bus, PTY emulation, kernel interfaces, memory safety, IPC |
| **Rust** | Concurrent architectures, transaction engines, Write-Ahead Logging, CLI/TUI tools |
| **Flutter & Mobile** | Reactive state architectures, offline-first sync, Bluetooth Low Energy (BLE), mesh networks |
| **Local AI & Edge Compute** | Edge LLM inference offloading, USB coprocessor orchestration, GGUF/llama.cpp |
| **Software Architecture** | Atomic swaps, LIFO rollback journals, traversal containment, clean APIs |

---

## Featured Projects

### [Woderrise](https://github.com/JustPirate/Woderrise)
**GitHub-Powered Linux Desktop Configuration Store**

A declarative Wayland dotfile center and configuration store in Rust with a native Iced (v0.14+) GUI. Eliminates multi-gigabyte monolithic clones by querying the Git Trees API and streaming targeted assets via commit-pinned Fastly CDN endpoints (0 REST quota). Features a 4-phase atomic swap transaction engine, Write-Ahead Logging (WAL), automatic pre-flight backups, and 1-click reversible LIFO rollbacks.

**Stack:** Rust · Iced v0.14+ · Tokio · Wayland · Fastly CDN · WAL

---

### [Nexus Net](https://github.com/JustPirate/nexius)
**Gaming Network Optimizer & Traffic Isolation Engine**

Cross-platform desktop application designed to measure live network adapter telemetry (RTT, jitter, packet loss via async ICMP/UDP), dynamically prioritize optimal physical network interfaces, and enforce strict application traffic lockdown to eliminate latency spikes and bufferbloat during competitive play.

**Stack:** Rust · Tauri · Tokio · Network HAL · Cross-Platform Sockets

---

### [PocketBridge](https://github.com/JustPirate/PocketBridge)
**Android Edge AI Coprocessor Bridge**

Turns idle Android phones into hardware-accelerated local coprocessors over high-speed USB (AOA / ADB). Streams GGUF quantized models to phone NPU/GPU backends, balancing LLM inference tasks between host desktops and mobile devices with zero cloud dependency.

**Stack:** Rust · C++ · llama.cpp · Android NDK · USB AOA · RPC

---

### [AgentControll](https://github.com/JustPirate/AgentControll)
**Local-First Control Plane for Coding Agents**

Supervisor daemon and Ratatui terminal interface managing the lifecycle of coding agents (Google Antigravity, Claude Code, Codex). Handles PTY stream emulation, multi-account profile isolation, quota tracking, permission automation, and SQLite audit event streams.

**Stack:** Rust · Ratatui · PTY · Tokio · SQLite · IPC

---

### [Safent (Travel SOS Mesh)](https://github.com/JustPirate/Safent)
**Offline Emergency Mesh Network System**

An offline-first emergency SOS mobile application designed for dead zones and natural disasters. Automatically switches from cellular/Wi-Fi to peer-to-peer Bluetooth Low Energy (BLE) mesh routing to propagate encrypted distress packets through nearby nodes until connectivity is restored.

**Stack:** Flutter · Dart · BLE Mesh · SharedPreferences · Location Services

---

### [ForgeX](https://github.com/JustPirate/ForgeX)
**Behavioral Accountability & Character Development System**

An empirical character development platform connecting declared commitments, active window monitoring, consequences, and recovery into an adaptive feedback loop. Features a background Linux activity watcher, Ratatui TUI, and Flutter companion client.

**Stack:** Rust · SQLite · Axum · Ratatui · Flutter · Dart FFI

---

### [Netra](https://github.com/JustPirate/Netra)
**Linux Connectivity & Audio Control Center**

Unified Linux desktop control center for managing Wi-Fi, Bluetooth, hotspot tethering, audio routing, and network diagnostics over system D-Bus services.

**Stack:** Rust · Linux · D-Bus · NetworkManager · PipeWire

---

## Technical Stack

**Languages**  
`Rust` `Dart` `Python` `C/C++` `SQL` `TypeScript`

**Systems & Platforms**  
`Linux (Arch/Debian)` `Wayland` `D-Bus` `PipeWire` `PTY` `BLE` `USB AOA`

**Frameworks & UI**  
`Iced (v0.14+)` `Ratatui` `Tauri` `Flutter` `React` `Tailwind CSS`

**Databases & Storage**  
`SQLite` `Hive` `Write-Ahead Logging (WAL)` `Local-First Storage`

---

## Engineering Principles

- **Understand before abstracting:** Learn kernel and OS interfaces directly before layering frameworks.
- **Fail-safe by default:** Use Write-Ahead Logs, automatic backups, and reversible transactions for state changes.
- **Local-first & private:** Value edge compute, local storage, and user privacy over mandatory cloud dependencies.
- **Zero warnings & high verification:** Clean compilation, strict linting, and thorough test coverage.

---

<div align="center">

[Portfolio](https://vijaygovindbiju.github.io/portfolio/) &nbsp;·&nbsp; [GitHub](https://github.com/JustPirate)

</div>
