from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from bidding.forms import BiddingForm
from .models import Bidding


@login_required
def biddings_view(request):
    """
    Handle a request to view a user's bidding.
    """
    biddings = Bidding.objects.all()
    return render(request, 'bidding/index.html', {
        'biddings': biddings,
    })


@login_required
def bidding_view(request, bidding_id):
    """
    Handle a request to view a user's bidding.
    """
    try:
        bidding = Bidding.objects.filter(
            user=request.user).get(id=bidding_id)
    except Bidding.DoesNotExist:
        raise Http404
    return render(request, 'bidding/bidding_view.html', {
        'bidding': bidding,
    })

@login_required
def bidding_create_view(request):
    """
    Handle a request to create a new bidding item.
    """
    if request.method == 'POST':
        form = BiddingForm(request.POST)
        if form.is_valid():
            new_bidding = form.save(commit=False)
            new_bidding.user = request.user
            print(new_bidding)
            new_bidding.save() 

            return redirect(biddings_view)
    else:
        form = BiddingForm()

    return render(request, 'bidding/bidding_create.html', {'form': form})


@login_required
def bidding_edit_view(request, bidding_id):
    """
    Handle a request to edit a bidding item.

    :param bidding_id: The database ID of the BiddingItem to edit.
    """
    template_dict = {}
    try:
        bidding = Bidding.objects.filter(
            user=request.user).get(id=bidding_id)
    except Bidding.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        if 'delete' in request.POST:
            bidding.delete()
            return redirect(biddings_view)

        form = BiddingForm(request.POST, instance=bidding)
        if form.is_valid():
            form.save()
            form = BiddingForm(instance=bidding)
            template_dict['message'] = 'Bidding Updated'
    else:
        form = BiddingForm(instance=bidding)

    template_dict['form'] = form
    template_dict['bidding_id'] = bidding_id

    return render(request, 'bidding/bidding_edit.html', template_dict)
