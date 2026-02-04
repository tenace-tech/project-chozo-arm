# Project Chozo: 6-DOF Robotic Arm

**A precision robotic manipulator built with LEGO Technic hardware, custom 3D printed parts, and a custom Python "Split-Brain" architecture.**

## 🎯 Project Goals
* **Hardware:** 6 Degrees of Freedom using LEGO Robot Inventor (51515) and Liebherr (42100) motors.
* **Software:** Custom Python driver with Hardware Abstraction Layer (HAL) for seamless development on Windows/Linux.
* **AI:** "Project Mammon" integration for local computer vision and object detection.

## 🏗 Architecture
* **Controller:** Raspberry Pi 4 (Headless) running Raspberry Pi OS Lite (64-bit).
* **Drivers:** `buildhat` library for direct motor control via GPIO.
* **Kinematics:** Custom inverse kinematics engine (In Progress).

## 🛠 Hardware & Fabrication
* **Actuators:** LEGO Robot Inventor (51515) & Liebherr (42100) motors.
* **Custom Parts:** Hybrid construction using **3D printed structural components** designed to interface with LEGO Technic geometry.
* **Controller:** Raspberry Pi 4 Model B (4GB).

## 🚀 Getting Started (Simulation)
You can run the full flight software in "Simulation Mode" on any PC without the hardware attached.

```bash
# Clone the repo
git clone [https://github.com/tenace-tech/project-chozo-arm](https://github.com/tenace-tech/project-chozo-arm)
cd project-chozo-arm

# Setup Environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Launch the CLI
python3 -m src.cli