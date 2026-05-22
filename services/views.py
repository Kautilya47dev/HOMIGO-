from django.shortcuts import render, get_object_or_404
from .models import Service, Booking, AMCBooking
from .forms import RegisterForm
from django.shortcuts import redirect

def home(request):

    services = Service.objects.all()

    return render(request, 'home.html', {
        'services': services
    })


def book_service(request, service_id):

    service = get_object_or_404(
        Service,
        id=service_id
    )

    recommendation = None

    # SMART CROSS-SELL LOGIC

    if 'AC' in service.name:

        recommendation = {
            'title': 'AC AMC Protection Plan',
            'offer': '20% OFF',
            'description':
            'Protect your AC with yearly servicing and gas checks.'
        }

    elif 'Refrigerator' in service.name:

        recommendation = {
            'title': 'Refrigerator AMC',
            'offer': 'Save ₹500',
            'description':
            'Prevent cooling issues with scheduled maintenance.'
        }

    elif 'RO' in service.name:

        recommendation = {
            'title': 'RO Maintenance Plan',
            'offer': 'Free Filter Cleaning',
            'description':
            'Keep water quality pure with regular servicing.'
        }

    elif 'Laptop' in service.name:

        recommendation = {
            'title': 'Laptop Protection Plan',
            'offer': '15% OFF',
            'description':
            'Regular servicing and hardware checkups.'
        }

    if request.method == 'POST':

        Booking.objects.create(

            service=service,

            customer_name=request.POST.get(
                'customer_name'
            ),

            phone_number=request.POST.get(
                'phone_number'
            ),

            address=request.POST.get(
                'address'
            )
        )

        return render(
            request,
            'success.html'
        )

    return render(request, 'booking.html', {

        'service': service,
        'recommendation': recommendation
    })


def amc(request):

    plans = []
    appliance = ""
    timeline = ""
    health_score = ""
    risk_level = ""
    maintenance_cost = ""
    recommendation_reason = ""

    if request.method == 'POST':

        timeline = request.POST.get('timeline')
        appliance = request.POST.get('appliance')

        # SMART LOGIC

        if timeline == '1998-2005':

            health_score = "45%"
            risk_level = "High"
            maintenance_cost = "₹5000 - ₹9000 yearly"

            recommendation_reason = (
                "Older appliances usually need "
                "frequent servicing and repairs."
            )

            if appliance == 'Refrigerator':

                plans = [
                    {
                        'name': 'Premium 2 Year AMC',
                        'price': '₹3499',
                        'benefits':
                        'Unlimited servicing + emergency support'
                    },
                    {
                        'name': '1 Year Protection Plan',
                        'price': '₹2499',
                        'benefits':
                        '4 maintenance visits + technician priority'
                    }
                ]

            elif appliance == 'AC':

                plans = [
                    {
                        'name': 'AC Premium Care',
                        'price': '₹3999',
                        'benefits':
                        'Gas refill + deep cleaning + emergency repair'
                    }
                ]

            elif appliance == 'RO':

                plans = [
                    {
                        'name': 'RO Total Care',
                        'price': '₹2499',
                        'benefits':
                        'Filter replacement + unlimited maintenance'
                    }
                ]

        elif timeline == '2015-2020':

            health_score = "70%"
            risk_level = "Medium"
            maintenance_cost = "₹2000 - ₹5000 yearly"

            recommendation_reason = (
                "Moderately aged appliances "
                "need preventive maintenance."
            )

            if appliance == 'Refrigerator':

                plans = [
                    {
                        'name': 'Premium Plan (1 Year)',
                        'price': '₹1999',
                        'benefits':
                        '4 visits + priority technician'
                    },
                    {
                        'name': 'Basic Plan (6 Months)',
                        'price': '₹999',
                        'benefits':
                        '2 maintenance visits'
                    }
                ]

            elif appliance == 'AC':

                plans = [
                    {
                        'name': 'Comfort Plan (1 Year)',
                        'price': '₹2499',
                        'benefits':
                        '4 services + deep cleaning'
                    }
                ]

            elif appliance == 'RO':

                plans = [
                    {
                        'name': 'Pure Water Plan',
                        'price': '₹1299',
                        'benefits':
                        'Filter cleaning + maintenance'
                    }
                ]

        else:

            health_score = "90%"
            risk_level = "Low"
            maintenance_cost = "₹800 - ₹2000 yearly"

            recommendation_reason = (
                "Newer appliances generally "
                "require less maintenance."
            )

            if appliance == 'Refrigerator':

                plans = [
                    {
                        'name': 'Basic Plan (6 Months)',
                        'price': '₹799',
                        'benefits':
                        'Basic maintenance support'
                    }
                ]

            elif appliance == 'AC':

                plans = [
                    {
                        'name': 'Cooling Care',
                        'price': '₹1499',
                        'benefits':
                        '2 AC services + gas check'
                    }
                ]

            elif appliance == 'RO':

                plans = [
                    {
                        'name': 'RO Care Lite',
                        'price': '₹899',
                        'benefits':
                        'Basic filter cleaning'
                    }
                ]

    return render(request, 'amc.html', {

        'plans': plans,
        'appliance': appliance,
        'timeline': timeline,
        'health_score': health_score,
        'risk_level': risk_level,
        'maintenance_cost': maintenance_cost,
        'recommendation_reason': recommendation_reason
    })

def book_amc(request):

    if request.method == 'POST':

        # Final booking form submitted
        if request.POST.get('customer_name'):

            AMCBooking.objects.create(

                customer_name=request.POST.get('customer_name'),

                phone_number=request.POST.get('phone_number'),

                address=request.POST.get('address'),

                appliance=request.POST.get('appliance'),

                timeline=request.POST.get('timeline'),

                selected_plan=request.POST.get('selected_plan')
            )

            return render(request, 'success.html')

        # From AMC plans page
        selected_plan = request.POST.get('selected_plan')
        timeline = request.POST.get('timeline')
        appliance = request.POST.get('appliance')

        return render(request, 'book_amc.html', {

            'selected_plan': selected_plan,

            'timeline': timeline,

            'appliance': appliance
        })

    return render(request, 'amc.html')
from .models import Booking, AMCBooking


def dashboard(request):

    service_bookings = Booking.objects.all().order_by('-id')

    amc_bookings = AMCBooking.objects.all().order_by('-id')

    context = {
        'service_bookings': service_bookings,
        'amc_bookings': amc_bookings,
    }

    return render(
        request,
        'dashboard.html',
        context
    )
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})