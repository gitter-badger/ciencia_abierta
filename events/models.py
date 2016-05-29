from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    EVENT_TYPE_LECTURE = 1
    EVENT_TYPE_MASTER_CLASS = 2
    EVENT_TYPE_EXCURSION = 3
    EVENT_TYPE_SHOW = 4
    EVENT_TYPE_ROUND_TABLE = 5
    EVENT_TYPE_CONFERENCE = 6
    EVENT_TYPE_MEETING = 7
    EVENT_TYPES = (
        (EVENT_TYPE_LECTURE, 'Lecture'),
        (EVENT_TYPE_MASTER_CLASS, 'Master class'),
        (EVENT_TYPE_EXCURSION, 'Excursion'),
        (EVENT_TYPE_SHOW, 'Show'),
        (EVENT_TYPE_ROUND_TABLE, 'Round table'),
        (EVENT_TYPE_CONFERENCE, 'Conference'),
        (EVENT_TYPE_MEETING, 'Meeting'),
    )

    EVENT_TOPIC_DESIGN = 1
    EVENT_TOPIC_CITY = 2
    EVENT_TOPIC_SCIENCE = 3
    EVENT_TOPIC_ART = 4
    EVENT_TOPIC_BUSINESS = 5
    EVENT_TOPIC_SOCIETY = 6
    EVENT_TOPIC_TECHNOLOGY = 7
    EVENT_TOPIC_MEDIA = 8
    EVENT_TOPIC_CULTURE = 9
    EVENT_TOPIC_PHOTOGRAPHY = 10
    EVENT_TOPIC_CINEMA = 11
    EVENT_TOPICS = (
        (EVENT_TOPIC_DESIGN, 'Design'),
        (EVENT_TOPIC_CITY, 'City'),
        (EVENT_TOPIC_SCIENCE, 'Science'),
        (EVENT_TOPIC_ART, 'Art'),
        (EVENT_TOPIC_BUSINESS, 'Business'),
        (EVENT_TOPIC_SOCIETY, 'Society'),
        (EVENT_TOPIC_TECHNOLOGY, 'Technology'),
        (EVENT_TOPIC_MEDIA, 'Media'),
        (EVENT_TOPIC_CULTURE, 'Culture'),
        (EVENT_TOPIC_PHOTOGRAPHY, 'Photography'),
        (EVENT_TOPIC_CINEMA, 'Cinema'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    event_type = models.PositiveSmallIntegerField(choices=EVENT_TYPES)
    topic = models.PositiveSmallIntegerField(choices=EVENT_TOPICS)
    event_date = models.DateTimeField()
    price = models.PositiveIntegerField()
    image = models.ImageField()
    speakers = models.ManyToManyField('events.Speaker')
    organizers = models.ManyToManyField('events.Organizers')
    city = models.ForeignKey('places.City')
    place = models.ForeignKey('places.Place')
    # tags
    # created_at
    # updated_at
    # is_published
    # created_by
    # is_approved
    # approved_by
