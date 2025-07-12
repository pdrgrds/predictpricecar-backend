from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CreditEvaluation
from .serializers import CreditEvaluationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class CreateCreditEvaluationAPIView(APIView):
    """
    API para registrar una evaluación de crédito
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CreditEvaluationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCreditEvaluationAPIView(APIView):
    """
    API para registrar una solicitud de crédito
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CreditEvaluationSerializer(data=request.data)
        if serializer.is_valid():
            evaluation = serializer.save(user=request.user)

            # Si marcó que desea ser contactado
            if evaluation.contact:
                subject = "Confirmación de solicitud de crédito"
                html_message = render_to_string("emails/credit_request_confirmation.html", {
                    "user": request.user,
                    "amount": evaluation.amount,
                    "term": evaluation.term,
                })
                plain_message = strip_tags(html_message)

                send_mail(
                    subject,
                    plain_message,
                    None,
                    [request.user.email],
                    html_message=html_message
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
