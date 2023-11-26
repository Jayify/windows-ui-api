using System;
using System.Windows.Automation;

class Program
{
    static void Main()
    {
        // Find the calculator process
        AutomationElement calculator = AutomationElement.RootElement.FindFirst(
            TreeScope.Children, new PropertyCondition(AutomationElement.NameProperty, "Calculator"));

        if (calculator != null)
        {
            // Find the "1" button
            AutomationElement button1 = calculator.FindFirst(
                TreeScope.Descendants, new PropertyCondition(AutomationElement.NameProperty, "1"));

            // Invoke the button (simulate a click)
            InvokePattern invokePattern = button1.GetCurrentPattern(InvokePattern.Pattern) as InvokePattern;
            invokePattern?.Invoke();
        }
        else
        {
            Console.WriteLine("Calculator not found.");
        }
    }
}