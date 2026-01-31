# 📦 Project Chozo: Bill of Materials

## 1. Core Hardware & Source Sets
*These sets provide the motors, actuators, and structural foundation.*

| Item                      | Qty | Description               | Usage                                                                                                         |
| :------------------------ | :-- | :------------------------ | :------------------------------------------------------------------------------------------------------------ |
| **LEGO Technic 42100**    | 1   | Liebherr R 9800 Excavator | Source for 3x XL Motors, 4x L Motors, 6x Large Actuators, 2x Mini Actuators, Turntable, and Structural Beams. |
| **LEGO MINDSTORMS 51515** | 1   | Robot Inventor Kit        | Source for Smart Hub (6-Port), 4x Medium Angular Motors (Teal), Distance/Color Sensors.                       |

## 2. Computing & Control
*The "Split-Brain" architecture: Pi handles high-level logic/vision; Hub handles inverse kinematics/motor control.*

| Item | Qty | Description | Usage |
| :--- | :--- | :--- | :--- |
| **Raspberry Pi 4 Model B** | 1 | 4GB RAM | Main "Spine" (Camera Streamer, Serial Bridge). |
| **Raspberry Pi Build HAT** | 1 | Official LEGO Technic Driver | Interface for 42100 Motors (Base, Shoulder, Waist). |
| **Robot Inventor Hub** | 1 | From Set 51515 | Interface for Arm Motors (Elbow, Wrist, Gripper). |
| **SD Card** | 1 | 32GB+ High Endurance | Boot drive (Raspberry Pi OS Lite). |

## 3. Vision & Sensors
*The sensory inputs for "Mammon" (Object Detection) and physical homing.*

| Item                    | Qty        | Description           | Usage                                                              |
| :---------------------- | :--------- | :-------------------- | :----------------------------------------------------------------- |
| **Pi Camera Module 3**  | 1          | **Wide** Lens Edition | Primary vision sensor. Wide lens required for workspace coverage.  |
| **Camera Ribbon Cable** | 1          | 50cm (CSI/DSI)        | Extended length to route through the arm to the wrist.             |
| **Tactile Switches**    | 3          | 6mm Momentary         | Physical limit switches for Waist, Shoulder, and Elbow homing.     |
| **Silicone Wire**       | Assortment | 30 AWG (Stranded)     | Flexible wiring for limit switches (routed through arm internals). |

## 4. Power & Connectivity
*Infrastructure for power delivery and data synchronization.*

| Item | Qty | Description | Usage |
| :--- | :--- | :--- | :--- |
| **Build HAT Power Supply** | 1 | 48W (8V / 6A) | **Critical:** Powers the Build HAT and 42100 Motors. |
| **Micro-USB Cable** | 1 | **Data Capable** | Connects Robot Inventor Hub to Raspberry Pi (Serial Comm). |
| **Ethernet Cable** | 1 | Flat / Ribbon Style (Cat6/7) | Direct low-latency SSH connection from Host Laptop to Pi. |
| **LEGO Extension Cables** | 2-4 | 25cm Power Functions | Extends reach for Base motors to the Build HAT. |

## 5. Mechanical Hardware
*Non-LEGO components for high-precision joints.*

| Item                 | Qty        | Description          | Usage                                                                          |
| :------------------- | :--------- | :------------------- | :----------------------------------------------------------------------------- |
| **Bearing 6706-2RS** | 1          | 30x37x4mm            | **Hollow Wrist Roll:** Allows cabling to pass through the center of the wrist. |
| **Bearing 683-2RS**  | 4-6        | 3x7x3mm              | **Gripper Linkage:** Frictionless pivot points for the fingers.                |
| **M3 Screws**        | Assortment | Button Head (6-20mm) | Main structural assembly for printed parts.                                    |
| **M3 Nuts**          | Assortment | Nylon Lock Nuts      | Secures moving linkages (prevents loosening).                                  |
| **M3 Washers**       | Assortment | M3x6mm               | Spread load without interfering with the bearings.                             |
| **M2.5 Screws**      | 4          | 6mm-10mm             | Mounting the Raspberry Pi / Build HAT to the chassis.                          |

## 6. 3D Printing Materials (Filament)
*Color-coded materials for computer vision segregation.*

| Color           | Material | Description | Usage                                                                  |
| :-------------- | :------- | :---------- | :--------------------------------------------------------------------- |
| **Orange**      | ASA      | Structural  | Main arm links (Matches LEGO "Construction Orange").                   |
| **White**       | ASA      | Structural  | High-contrast accents.                                                 |
| **Black**       | ASA      | Structural  | Hidden structural parts.                                               |
| **Neon Purple** | TPU      | Flexible    | **Gripper Pads:** High-friction & "Identity Tag" for Vision System.    |
| **Green**       | PLA      | Rigid       | **Calibration Blocks:** "Green Screen" color for coordinate artifacts. |
