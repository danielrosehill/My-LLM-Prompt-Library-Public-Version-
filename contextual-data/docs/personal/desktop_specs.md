# Context Snippet: My Desktop Spec

![alt text](../../../images/repair-sloth.webp)

A very simple but highly useful "context snippet" to have on hand is a simple list of your computer's parameters.

Go all out and create one for every device you own!

A tip: Note your OS too or anything else about the software you're running that might effect what this context snippet could come in useful for.

## How to use this context in prompts

I have my desktop spec saved as `mydesktop.md` and use this snippet all the time when prompting. 

Because it notes my Linux distro *and* my hardware, it makes finding compatible *anything* vastly quicker and easier.

A prompt might go something like:

> Here are the specs of my desktop computer. Can you recommend a GPU upgrade?

(The useful context here includes everything from your PSU to motherboard to, of course, your OS)

Or:

> This is my computer. I want to buy a UPS. What capacity should be sufficient?


## Don't forget!

Keep this snippet updated as your hardware evolves / you upgrade components / etc. 

## Model Context Snippet

Usage: generate your own spec, save to your "context repo" / vector database / RAG system / whatever takes your fancy.

(Recommended formats: `json`, `md` etc)

| **Component**    | **Specification**                                            |
| ---------------- | ------------------------------------------------------------ |
| **CPU**          | Intel Core i7-12700F 2.1GHz 25MB 1700 Tray                   |
| **Motherboard**  | Pro B760M-A WiFi 1700 DDR5 MSI B760 Chip                     |
| **RAM**          | 64GB as 16GB x 4 Kingston DDR5 4800MHz (Model: KVR48U40BS8-16) |
| **Storage**      | NVME x 1.1 TB <br> SSD x 2 1TB <br> BTRFS                    |
| **GPU**          | AMD Radeon RX 7700 XT Pulse Gaming 12GB Sapphire             |
| **Power Supply** | Gold 80+ MDD Focus GX-850 850W Seasonic                      |
| **Case**         | Pure Base 500 Be Quiet                                       |
| **CPU Cooler**   | Pure Rock 2 Be Quiet                                         |

## OS and Filesystem

| **OS**         | OpenSUSE Tumbleweed (X11, KDE Plasma) |
| -------------- | ------------------------------------- |
| **Filesystem** | BTRFS                                 |