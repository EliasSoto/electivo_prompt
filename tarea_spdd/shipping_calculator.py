class ShippingCalculator:

    @staticmethod
    def calculate_shipping(cart_total, is_express, destination):
        if destination not in ("NATIONAL", "INTERNATIONAL"):
            raise ValueError(f"Destino desconocido: {destination}")

        shipping_cost = 10.0 if cart_total < 100.0 else 0.0

        if is_express:
            shipping_cost += 15.0

        if destination == "INTERNATIONAL":
            shipping_cost *= 2.0

        return shipping_cost