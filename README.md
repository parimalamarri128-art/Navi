# Navi — Windows Desktop Assistant

Navi is a Python-based Windows desktop assistant that lets users perform common computer tasks using simple commands.

## ✨ Features

* 🌐 Open websites
* 🔎 Google and YouTube search
* 📁 Create folders
* 📄 Create files
* ✏️ Rename files and folders
* 📋 Copy files and folders
* 🚚 Move files and folders
* 🗑️ Delete files and folders with confirmation
* 🖼️ Search images by name
* 🎬 Search videos
* 📑 Search PDF files
* 📄 Search documents
* 🔍 Search files by name
* 📂 Open search results using commands such as `open 1`, `open 2`
* 📄 Find and open resume files
* 🖥️ Open supported Windows applications
* ⚙️ Basic Windows system controls

## 💻 Requirements

* Windows
* Python 3.10 or later
* Git
* VS Code (recommended)

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/parimalamarri128-art/Navi.git
```

Open the Navi folder:

```bash
cd Navi
```

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

Run Navi:

```bash
python main.py
```

## 🎯 Example Commands

### 🌐 Websites

```text
open youtube
open gmail
open github
```

### 📄 Files

```text
create file test.txt
rename test.txt to newtest.txt
copy newtest.txt to Desktop
move newtest.txt to Downloads
delete newtest.txt
```

### 📁 Folders

```text
create folder TestNavi
rename TestNavi to NewNavi
copy NewNavi to Desktop
move NewNavi to Downloads
delete NewNavi
```

### 🔎 Search

```text
my photos
my videos
my pdfs
my documents
find my resume
```

After a search, Navi can open a specific result:

```text
open 1
open 2
open 3
```

## 🛡️ Safe Delete Confirmation

Before deleting a file or folder, Navi asks for confirmation.

Example:

```text
Navi: I found:
C:\Users\PC\Documents\Navi\newnavi

Are you sure you want to delete it?
Reply with yes or no.
```

The user can respond with:

```text
yes
```

or:

```text
no
```

## 🧩 Project Structure

```text
Navi/
├── ai.py
├── app_manager.py
├── browser_manager.py
├── file_manager.py
├── intent_manager.py
├── main.py
├── requirements.txt
├── settings.py
├── system_manager.py
├── ui.py
├── utils.py
├── voice.py
├── README.md
├── LICENSE
└── .gitignore
```

## 🛣️ Roadmap

Future versions may include:

* 🎤 Improved voice commands
* 🧠 Better natural-language understanding
* 🤖 AI-powered assistance
* ⚙️ More Windows automation
* 🧑‍💻 Developer tools
* 🎫 Developer ticket and issue assistance
* 🔗 Integration with developer platforms
* 🔌 More application integrations

## 🧪 Current Version

**v1.0.0**

This is the first public release of Navi.

## 📜 License

Navi is released under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Project

Navi is an experimental Windows assistant project focused on making common computer operations easier through simple commands.

Contributions, suggestions, and improvements are welcome.

## ⭐ Support

If you find Navi useful, consider giving the repository a ⭐ on GitHub.

Repository:

https://github.com/parimalamarri128-art/Navi
