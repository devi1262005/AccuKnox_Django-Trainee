from django.core.management.base import BaseCommand
from django.db import transaction
from Q3app.models import CartItem
import threading

class Command(BaseCommand):
    help = "Menu-driven shopping cart simulation"

    def handle(self, *args, **kwargs):
        print(f"Caller thread: {threading.current_thread().name}")

        while True:
            print("\nShopping Cart Menu:")
            print("1. Insert item")
            print("2. Update item")
            print("3. Delete item")
            print("4. Exit and Display")

            choice = input("Enter choice: ")

            try:
                with transaction.atomic():
                    if choice == "1":
                        name = input("Item name: ")
                        qty = int(input("Quantity: "))
                        CartItem.objects.create(name=name, quantity=qty)

                    elif choice == "2":
                        name = input("Item to update: ")
                        item = CartItem.objects.get(name=name)
                        new_qty = int(input("New quantity: "))
                        item.quantity = new_qty
                        item.save()

                    elif choice == "3":
                        name = input("Item to delete: ")
                        item = CartItem.objects.get(name=name)
                        del_qty = int(input(f"Quantity to delete (current {item.quantity}): "))
                        if del_qty >= item.quantity:
                            item.delete()
                        else:
                            item.quantity -= del_qty
                            item.save()

                    elif choice == "4":
                        print("\nFinal Committed Order:")
                        items = CartItem.objects.all()
                        if items.exists():
                            for item in items:
                                print(f"- {item.name}: {item.quantity}")
                        else:
                            print("Cart is empty")
                        print("Exiting...")
                        break

                    else:
                        print("Invalid choice! Please select 1-4.")

            except Exception as e:
                print(f"Transaction rolled back due to: {e}")
