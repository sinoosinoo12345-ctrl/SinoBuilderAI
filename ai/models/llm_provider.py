from __future__ import annotations

from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str
    ) -> str:
        pass


class MockProvider(BaseLLMProvider):
    """
    Universal local AI code generator.
    """

    def generate(
        self,
        prompt: str
    ) -> str:

        text = prompt.lower()


        # =====================================
        # CODE GENERATION FIRST
        # =====================================

        if (
            "generate production" in text
            or "source code" in text
            or "generate code" in text
        ):


            # -----------------
            # Python
            # -----------------

            if ".py" in text:


                if "auth" in text:
                    return """
from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/login")
def login(data: dict):

    return {
        "success": True,
        "user": data
    }
"""


                if "models" in text:
                    return """
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Model:

    id: int
"""


                if "database" in text:
                    return """
from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///app.db"

engine = create_engine(
    DATABASE_URL
)
"""


                if "payment" in text:
                    return """
from fastapi import APIRouter


router = APIRouter()


@router.post("/payment")
def payment(data: dict):

    return {
        "status": "paid",
        "data": data
    }
"""


                return """
from fastapi import FastAPI


app = FastAPI(
    title="AI Generated Application"
)


@app.get("/")
def root():

    return {
        "status": "running"
    }
"""


            # -----------------
            # Dart Flutter
            # -----------------

            if ".dart" in text:

                return """
import 'package:flutter/material.dart';


void main(){

  runApp(
    const App()
  );

}


class App extends StatelessWidget{

  const App({
    super.key
  });


  @override
  Widget build(
    BuildContext context
  ){

    return MaterialApp(

      home: Scaffold(

        body: Center(

          child: Text(
            "AI Generated App"
          )

        )

      )

    );

  }

}
"""



        # =====================================
        # AGENTS
        # =====================================


        if "planner" in text:

            return """
PROJECT PLAN

Requirements analysis.
Architecture design.
Implementation.
Testing.
Deployment.
"""


        if "architect" in text:

            return """
SYSTEM ARCHITECTURE

Frontend
Backend
Database
AI Layer

Clean Architecture.
SOLID Principles.
"""


        if "security" in text:

            return """
SECURITY PLAN

JWT Authentication.
Authorization.
Data protection.
"""


        if "testing" in text:

            return """
TEST PLAN

Unit Tests.
API Tests.
Integration Tests.
"""



        return """
AI RESPONSE

Request analyzed successfully.
"""
