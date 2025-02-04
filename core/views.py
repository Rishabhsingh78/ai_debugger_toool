from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .utils import execute_code
from .ai_helper import analyze_error

class DebugCodeView(APIView):
    parser_classes = [JSONParser]
    def post(self,request):
        code = request.data.get("code","")
        if not code:
            return Response({'eroor':'No code provided'},status=400)
        
        result = execute_code(code)

        if result["status"] == "error":
            ai_suggestion = analyze_error(result['traceback'])

            return Response({
                "error_message": result["error_message"],
                "traceback": result["traceback"],
                "ai_suggestion": ai_suggestion
            })

        return Response({"message": result["message"]})