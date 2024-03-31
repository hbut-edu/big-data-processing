# 如何在Windows 11中打开WSL并安装基于WSL的Docker

在开始之前，请确保你的Windows 11满足以下版本要求：

- **Windows 11版本要求**：为了使用WSL2，你的系统需要运行Windows 11版本21H2或更高版本。此外，确保系统支持虚拟化技术，并且在BIOS中启用了此功能。

## 启用WSL

### 使用Windows功能启用WSL

1. **打开Windows功能**：打开“控制面板” > “程序” > “程序和功能” > “启用或关闭Windows功能”。
   
2. **启用WSL和虚拟机平台**：勾选“适用于Linux的Windows子系统”和“虚拟机平台”选项，然后点击“确定”并重启计算机。

### 使用命令行启用WSL

作为另一种选择，你也可以通过命令行启用WSL和虚拟化平台。这需要以管理员权限打开PowerShell。

1. **打开PowerShell**：右击开始按钮，选择“Windows PowerShell(管理员)”。

2. **启用WSL**：在PowerShell中输入以下命令并回车：
   ```powershell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   ```
3. **启用虚拟机平台**：接着，输入以下命令来启用虚拟机平台功能，并重启计算机：
   ```powershell
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```

4. **设置WSL2为默认版本**：安装完WSL后，你可能需要设置WSL2作为默认版本。在同一PowerShell窗口中输入以下命令：
   ```powershell
   wsl --set-default-version 2
   ```

## 安装Linux发行版

1. **打开Microsoft Store**：启用WSL后，打开Microsoft Store，搜索你想要的Linux发行版（例如Ubuntu、Debian等）。

2. **安装Linux发行版**：选择一个发行版，点击“获取”或“安装”，然后等待下载和安装过程完成。

3. **设置Linux发行版**：安装完成后，点击“启动”或从开始菜单中打开Linux发行版，首次启动时，系统将提示你创建一个用户帐户和密码。

## 安装Docker Desktop

1. **下载Docker Desktop**：访问Docker官网下载页面（[https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)），下载适用于Windows的Docker Desktop安装程序。

2. **安装Docker Desktop**：运行下载的安装程序，遵循安装向导的指示完成安装。

3. **配置Docker以使用WSL2**：安装完成后，启动Docker Desktop。在设置中，确保启用了“使用WSL 2 基础架构”选项（默认情况下通常是启用的）。

## 验证安装

1. **打开WSL终端**：通过开始菜单打开你安装的Linux发行版。

2. **运行Docker命令**：在WSL终端中，输入`docker run hello-world`来验证Docker是否正确安装并配置。如果安装成功，你将看到一条消息说明你的Docker安装正常工作。