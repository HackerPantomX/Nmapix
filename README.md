# Nmapix
Nmapix is a python based tool used for Scanning network and found weakness of target system and exploit them ! This tool help to exploit target device
<p align="center">
  <pre>
      o O ______________________
 _[]_|______________________N
|  O O O O      O O O O    \
+--(@)(@)------(@)(@)-------'
  </pre>
</p>

<h1 align="center">Nmapix 🚀</h1>
<h3 align="center">Advanced Python Nmap Security Framework & CLI Wrapper</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Nmapix-red.svg" alt="Framework">
  <img src="https://img.shields.io/badge/AI-Google%20Gemini-orange.svg" alt="Gemini AI">
  <img src="https://img.shields.io/badge/Status-Stable-green.svg" alt="Status">
</p>

---

## 🛠️ About Nmapix

**Nmapix** is a powerful, automated, and lightweight command-line security framework built natively using Python and the official `python-nmap` library. Designed for penetration testers, system administrators, and security enthusiasts, it streamlines network discovery, host enumeration, vulnerability checking, and interacts smartly with **Google Gemini AI** for real-time analysis.

---

## ✨ Key Features

* **Core Nmap Scans:** Automated execution of SYN Stealth Scans (`-sS`), Service & Version Detection (`-sV`), OS Detection (`-O`), UDP Scans (`-sU`), and Aggressive Scans (`-A`).
* **Advanced Reconnaissance:** Ping sweeps (`-sn`), vulnerability script checks (`--script vuln`), fast port scans (`-F`), and custom command execution.
* **Google Gemini AI Integration:** Interactive AI assistant powered by `google-genai` to help interpret scan outputs and troubleshoot networking queries.
* **Cross-Platform Compatibility:** Runs smoothly on Linux, Termux (Android), and mobile Python environments like Pydroid 3.
* **Clean & Safe Interface:** Styled with colorful CLI outputs (`colorama`), robust error handling, and safe exit routines (`Ctrl+C`).

---

## 📦 Installation & Setup

Run the following commands in your terminal (Linux / Termux) to clone and install the tool:

```bash
# Clone the repository
git clone [https://github.com/HackerPantomX/Nmapix.git](https://github.com/HackerPantomX/Nmapix.git)

# Navigate into the project directory
cd Nmapix

# Install required Python dependencies
pip install -r requirements.txt

