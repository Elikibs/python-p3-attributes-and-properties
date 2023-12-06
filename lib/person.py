#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self):
        self._job = None
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, job_type):
        if job_type not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = job_type

employee1 = Person()
employee1.job = "Marketing"
print(employee1.job)