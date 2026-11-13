<div align="center">

# ⚓ JustPirate

**Systems Engineer & Low-Level Toolmaker**  
*Building high-performance software from the kernel up.*

```rust
fn profile() -> Developer {
    Developer {
        handle: "JustPirate",
        focus: ["Systems Programming", "Linux Internals", "Rust Ecosystem", "Autonomous AI Agents", "Offline Mesh Networks"],
        motto: "Understand the hardware and kernel before abstracting.",
    }
}
```

<p align="center">
  <a href="https://github.com/JustPirate">
    <img src="https://img.shields.io/badge/GitHub-JustPirate-0D1117?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <img src="https://img.shields.io/badge/Language-Rust-CE412B?style=for-the-badge&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/OS-Linux_Kernel-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/Architecture-x86__64_/_ARM64-007ACC?style=for-the-badge" alt="Architecture" />
</p>

</div>

---

### 🌊 About Me

I am a software engineer focused on what happens beneath the surface: operating system interfaces, network kernels, runtime scheduling, and distributed protocols. I build tools where latency, memory safety, and fail-safe recovery are paramount.

- 🦀 **Rust & Systems:** Kernel policy routing (Netlink/WFP), raw socket telemetry, PTY emulation, and transactional journaling.
- 🐧 **Linux Desktop & Wayland:** Hyprland tooling, D-Bus service orchestration, PipeWire, and atomic desktop management.
- 🤖 **Agentic & AI Infrastructure:** Local-first terminal supervisors for autonomous coding agents, multi-account vaulting, and ADB compute offloading.
- 📡 **Offline Networking:** Zero-cloud peer-to-peer BLE mesh routing and high-speed USB-C hardware IPC.

---

### 🚀 Flagship Projects

<table>
  <tr>
    <td width="50%">
      <h3 align="center"><a href="https://github.com/JustPirate/nexius">🎯 Nexus Net (nexius)</a></h3>
      <p align="center"><b>Kernel Gaming Network Optimizer & Traffic Isolation</b></p>
      <p>High-performance cross-platform network engine built with <b>Rust & Tauri v2</b>. Features live multi-adapter telemetry (sliding window math), dynamic policy routing via Linux Netlink Table 100 and Windows WFP app redirection without dropping live connections, process-level firewall lockdown (nftables), and a fail-safe dead-man watchdog.</p>
      <p align="center">
        <code>Rust</code> · <code>Tauri v2</code> · <code>Netlink</code> · <code>nftables</code> · <code>WFP</code>
      </p>
    </td>
    <td width="50%">
      <h3 align="center"><a href="https://github.com/JustPirate/AgentControll">🤖 AgentControll</a></h3>
      <p align="center"><b>Local-First Supervisor for Coding Agents</b></p>
      <p>Control plane and terminal supervisor for autonomous coding agents (Antigravity, Claude Code, Devin CLI). Manages multi-agent sessions, isolates credentials per profile, automates quota failover/handoff, and features a full ANSI PTY terminal with SQLite audit event streaming.</p>
      <p align="center">
        <code>Rust</code> · <code>PTY</code> · <code>Tokio</code> · <code>SQLite</code> · <code>Ratatui</code>
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3 align="center"><a href="https://github.com/JustPirate/PocketBridge">⚡ PocketBridge</a></h3>
      <p align="center"><b>Android Compute & Coprocessor Offloader</b></p>
      <p>Enables compute and model offloading from a Linux host to an attached Android phone over a high-speed ADB link via USB-C on localhost. Rust host with a terminal UI paired with an Android worker, benchmarking real-world latency and throughput.</p>
      <p align="center">
        <code>Rust</code> · <code>Kotlin</code> · <code>ADB Protocol</code> · <code>USB-C IPC</code>
      </p>
    </td>
    <td width="50%">
      <h3 align="center"><a href="https://github.com/JustPirate/Woderrise">🐧 Woderrise</a></h3>
      <p align="center"><b>Transactional Hyprland Desktop Store</b></p>
      <p>A declarative Linux desktop customization store to discover, preview, and install Hyprland components with atomic transaction journaling, Write-Ahead Logging (WAL), pre-flight backups, and 1-click reversible LIFO rollbacks.</p>
      <p align="center">
        <code>Rust</code> · <code>Wayland</code> · <code>Hyprland</code> · <code>WAL Transactions</code>
      </p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <h3 align="center"><a href="https://github.com/JustPirate/Safent">🛡️ Safent (Offline Travel SOS Mesh)</a></h3>
      <p align="center"><b>Zero-Internet Emergency Mesh Network</b></p>
      <p>Offline-first safety companion that detects danger using phone sensors and risk fusion. Relays encrypted SOS distress packets through nearby peer devices over Bluetooth Low Energy (BLE) mesh until connectivity is restored, featuring a live responder dashboard.</p>
      <p align="center">
        <code>Dart</code> · <code>Flutter</code> · <code>BLE Mesh</code> · <code>Sensor Fusion</code> · <code>P2P Relays</code>
      </p>
    </td>
  </tr>
</table>

---

### 🛠️ Tech Stack & Arsenal

<div align="center">

| Domain | Technologies & Tools |
| :--- | :--- |
| **Core Languages** | ![Rust](https://img.shields.io/badge/Rust-CE412B?style=flat-square&logo=rust&logoColor=white) ![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black) ![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Dart](https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Shell](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white) |
| **Systems & Linux** | `Netlink (rtnetlink)` • `nftables` • `Windows WFP` • `Wayland / Hyprland` • `D-Bus` • `PTY` • `PipeWire` • `ethtool / iw` |
| **Frameworks & UI** | `Tauri v2` • `Ratatui` • `Tokio Async` • `Flutter` • `Iced` • `Axum` • `React` |
| **Data & Storage** | `SQLite` • `Write-Ahead Logging (WAL)` • `Protocol Buffers` • `Local-First Storage Engines` |

</div>

---

### 📊 GitHub Activity & Metrics

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=JustPirate&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub Stats" height="165" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=JustPirate&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" height="165" />
</div>

---

### ⚓ Engineering Invariants

> **1. Understand Before Abstracting:** Always master the raw kernel, socket, and memory primitives before adopting libraries.  
> **2. Fail-Safe by Default:** Every state modification must have transaction logs, rollback capability, and dead-man recovery hooks.  
> **3. Local-First & Sovereign:** Prioritize edge compute, local device communication, and user privacy over cloud dependency.  
> **4. Rigorous Empirical Verification:** Software is incomplete without stress tests, adversarial scenarios, and strict zero-warning compilation.

<div align="center">
  <sub>Crafted with precision by <b><a href="https://github.com/JustPirate">JustPirate</a></b></sub>
</div>
