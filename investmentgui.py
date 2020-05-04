"""
Program: investmentGUI.py
Author: Letisha Rahming
Date Created:   4/7/2020
Date Completed: 4/28/2020
Last Updated: 5/3/2020
Description: Gui based investment calculator (P3.276.277)
"""

from breezypythongui import EasyFrame

class investmentgui(EasyFrame):
    """investment calculator"""
    def __init__(self):
        EasyFrame.__init__(self, title = "Investment Calculator")
        #labels for the window
        self.addLabel(text = "Initial Amount ", row = 0, column = 0)
        self.addLabel(text = "Number of Years ", row = 1 , column = 0)
        self.addLabel(text = "Interest Rate in %", row = 2, column = 0)
        #enry fields
        self.amount = self.addFloatField(value = 0.0, row =0, column = 1)
        self.period = self.addIntegerField(value = 0, row =1, column = 1)
        self.rate = self.addIntegerField(value = 0, row = 2, column = 1)
        #text area widget
        self.outputArea = self.addTextArea(text = " ", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
        self.compute = self.addButton(text = "compute", row = 3, column = 0, columnspan = 2, command = self.compute)
    #event handling method
    def compute (self):
        """computes the investment schedule based on the inputs of the gui and then outputs the schedule in the text area"""
        #obtain and validate the inputs
        startBalance = self.amount.getNumber()
        rate = self.rate.getNumber()/100
        years = self.period.getNumber()
        if startBalance == 0 or rate == 0 or years == 0:
            return
        #set the header for the table
        result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")
        #Compute and append the results for each year
        totalInterest = 0.0
        for year in range (1, years + 1):
            interest = startBalance * rate
            endBalance = startBalance + interest
            result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
            #the ending balance for year 1 wil lbe the starting balance for year 2 and so on
            startBalance = endBalance
            totalInterest += interest
        #Append the totals for the entire period - final output for the whole thing
        result += "Ending Balance: $%0.2f\n" % endBalance
        result += "Total interest earned: $%0.2f\n" % totalInterest
        #Output the result while preserving read-only status
        self.outputArea["state"] = "normal"
        self.outputArea.setText(result)
        self.outputArea["state"] = "disabled"
def main():
    investmentgui().mainloop()
#global call to main
main()
        