# ⚓ JustPirate

> **Systems Engineer & Low-Level Toolmaker**  
> *Building high-performance software from the kernel up — Linux internals, Rust architectures, and local-first systems.*

---

### 🌊 Overview

I am a software engineer focused on what happens beneath the surface: operating system interfaces, network kernels, runtime scheduling, and distributed protocols. I build tools where latency, memory safety, and fail-safe recovery are paramount.

- 🦀 **Rust & Systems:** Kernel policy routing (Netlink/WFP), raw socket telemetry, PTY emulation, and transactional journaling.
- 🐧 **Linux Desktop & Wayland:** Hyprland tooling, D-Bus service orchestration, PipeWire, and atomic desktop management.
- 🤖 **Agentic & AI Infrastructure:** Local-first terminal supervisors for autonomous coding agents, multi-account vaulting, and ADB compute offloading.
- 📡 **Offline Networking:** Zero-cloud peer-to-peer BLE mesh routing and high-speed USB-C hardware IPC.

---

### 🚀 Featured Projects

| Project | Focus | Tech Stack | Highlights |
| :--- | :--- | :--- | :--- |
| **[🎯 Nexus Net (`nexius`)](https://github.com/JustPirate/nexius)** | Kernel Network Routing & Firewall Lockdown | `Rust` `Tauri v2` `Netlink` `nftables` `WFP` | Dynamic policy routing (Linux Table 100 / Windows WFP) without dropping TCP/UDP sessions, raw socket inspector, and fail-safe watchdog. |
| **[🤖 AgentControll](https://github.com/JustPirate/AgentControll)** | Local-First Supervisor for Coding Agents | `Rust` `PTY` `Tokio` `SQLite` `Ratatui` | Supervisor for Claude Code, Antigravity, and Devin CLI with multi-account isolation and automated quota failover. |
| **[⚡ PocketBridge](https://github.com/JustPirate/PocketBridge)** | Android Compute & AI Coprocessor Offloader | `Rust` `Kotlin` `ADB Protocol` `USB-C IPC` | Offloads compute from Linux hosts to attached Android phones over high-speed USB-C ADB localhost link. |
| **[🐧 Woderrise](https://github.com/JustPirate/Woderrise)** | Transactional Hyprland Desktop Store | `Rust` `Wayland` `Hyprland` `WAL Transactions` | Declarative Linux dotfile center with atomic transaction journaling, Write-Ahead Logging (WAL), and 1-click reversible rollbacks. |
| **[🛡️ Safent](https://github.com/JustPirate/Safent)** | Zero-Internet Emergency Mesh Network | `Dart` `Flutter` `BLE Mesh` `Sensor Fusion` | Offline-first SOS companion that propagates encrypted distress packets via Bluetooth Low Energy mesh without cellular connectivity. |

---

### 🛠️ Tech Stack & Arsenal

- **Languages:** `Rust` · `C` · `C++` · `Python` · `Dart` · `TypeScript` · `SQL` · `Bash`
- **Systems & Linux:** Netlink (`rtnetlink`) · `nftables` · Windows WFP · Wayland · Hyprland · D-Bus · PTY Emulation · PipeWire · `ethtool` / `iw`
- **Frameworks & UI:** Tauri v2 · Ratatui · Tokio Async · Flutter · Iced · Axum · React
- **Data & Architecture:** SQLite · Write-Ahead Logging (WAL) · Protocol Buffers · Local-First Sync

---

### ⚓ Engineering Invariants

1. **Understand Before Abstracting:** Master raw kernel, socket, and memory primitives before adopting libraries.
2. **Fail-Safe by Default:** Every state modification must have transaction logs, rollback capability, and dead-man recovery hooks.
3. **Local-First & Sovereign:** Prioritize edge compute, local device communication, and user privacy over cloud dependency.
4. **Rigorous Empirical Verification:** Software is incomplete without stress tests, adversarial scenarios, and strict zero-warning compilation.
