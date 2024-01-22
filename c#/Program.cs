using System;
using System.Threading;
using WindowsInput;

class Program
{
    static void Main()
    {
        // Start Notepad
        Console.WriteLine("Starting Notepad...");
        System.Diagnostics.Process.Start("notepad.exe");
        Thread.Sleep(2000); // Wait for Notepad to open

        // Automate Notepad
        AutomateNotepad();

        Console.ReadLine(); // Keep the console window open
    }

    static void AutomateNotepad()
    {
        var inputSimulator = new InputSimulator();

        // Type some text
        Console.WriteLine("Typing text in Notepad...");
        inputSimulator.Keyboard.TextEntry("Hello, Windows Automation!");

        Thread.Sleep(1000); // Wait for the text to be typed

        // Save the file
        Console.WriteLine("Saving file...");
        inputSimulator.Keyboard.ModifiedKeyStroke(WindowsInput.Native.VirtualKeyCode.CONTROL, WindowsInput.Native.VirtualKeyCode.VK_S); // Ctrl+S (Save)

        Thread.Sleep(1000); // Wait for the save dialog to appear (adjust if needed)

        // Simulate typing a file name and press Enter (replace with a real file path)
        Console.WriteLine("Typing file name...");
        inputSimulator.Keyboard.TextEntry("MyAutomationFile.txt");
        inputSimulator.Keyboard.KeyPress(WindowsInput.Native.VirtualKeyCode.RETURN); // Press Enter
    }
}
