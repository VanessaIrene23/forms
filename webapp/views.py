from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def homePage(request):
    context = {
        "income": 0,
        "total_paye": 0,
        "total_nssf": 0,
        "total_deductions": 0,
        "net_income": 0,
    }
    
    if request.method == "POST":
        # Get the body for the post
        payload = request.POST
        income = payload.get("income")
        
        # Only process if income exists
        if income:
            # Convert the value of income to make sure its an integer
            income = int(income)
            
            # declare the percentages of the paye and nssf
            paye = 38/100  # 38%
            nssf = 10/100  # 10%
            
            # check income against the tax bracket and calculate
            if income < 210000:
                total_paye = 0
                total_nssf = 0
                total_deductions = 0
                net_income = income
            else:
                # calculate the paye and nssf
                total_paye = income * paye
                total_nssf = income * nssf  # Fixed: was using paye instead of nssf
                total_deductions = total_paye + total_nssf
                net_income = income - total_deductions
            
            # Update context with calculated values
            context = {
                "income": income,
                "total_paye": total_paye,
                "total_nssf": total_nssf,
                "total_deductions": total_deductions,
                "net_income": net_income,
            }
    
    # Single return statement at the end for both GET and POST requests
    return render(request, "home.html", context)