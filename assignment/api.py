from django.http import HttpResponse
from django.core import serializers
import json

from .models import Assignment, AssignmentInstance


def get_all_assignments(request, student_enroll_no, subject_id=None):
    if request.method != 'GET':
        return HttpResponse({'error': 'BAD REQUEST'}, content_type='text/json-comment-filtered')

    if request.method == 'GET':
        # TODO: Optimise the api
        # resp_data = {}
        assignment_instances = AssignmentInstance.objects.filter(student__enroll_no=student_enroll_no)

        if subject_id:
            assignment_instances = assignment_instances.filter(assignment__subject__id=2)

        # for assignment_instance in assignment_instances:
        #     assignment_instance_dict = {}
        #     assignment_instance_dict['assignment_details'] = json.dumps(
        #         Assignment.objects.filter(id=assignment_instance.assignment.id).values()[0])
        #     assignment_instance_dict['submit_time'] = json.dumps(assignment_instance.submit_time)
        #     assignment_instance_dict['file_uploaded'] = json.dumps(assignment_instance.file_uploaded)
        #     assignment_instance_dict['marks'] = json.dumps(assignment_instance.marks)
        #     assignment_instance_dict['remarks'] = json.dumps(assignment_instance.remarks)
        #     assignment_instance_dict['reviewed'] = json.dumps(assignment_instance.reviewed)
        #     resp_data[assignment_instance.id] = assignment_instance_dict

        assignments_json_data = serializers.serialize('json', assignment_instances)
        return HttpResponse(assignments_json_data, content_type='text/json-comment-filtered')
