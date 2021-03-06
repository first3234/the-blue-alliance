class NotificationType(object):
    """
    Constants regarding the different types of notification we can send to a device
    See https://docs.google.com/document/d/1SV-hNCtgAn2hSMZaC973UdLHCFXCNpvq_RKq0UoY4yg/edit#
    """

    # DO NOT CHANGE THESE CONSTANTS
    UPCOMING_MATCH = 0
    MATCH_SCORE = 1
    LEVEL_STARTING = 2
    ALLIANCE_SELECTION = 3
    AWARDS = 4
    MEDIA_POSTED = 5
    DISTRICT_POINTS_UPDATED = 6
    SCHEDULE_POSTED = 7
    FINAL_RESULTS = 8
    PING = 9  # This type of message is sent when the user hits 'ping device' in their account overview
    BROADCAST = 10  # Not yet implemented, but gives functionality for admins to send to many devices

    # These aren't notifications, but used for upstream API calls
    UPDATE_FAVORITES = 100
    UPDATE_SUBSCRIPTION = 101

    # This is used for verification that the proper people are in control
    VERIFICATION = 200

    type_names = {
        UPCOMING_MATCH: "upcoming_match",
        MATCH_SCORE: "match_score",
        LEVEL_STARTING: "starting_comp_level",
        ALLIANCE_SELECTION: "alliance_selection",
        AWARDS: "awards_posted",
        MEDIA_POSTED: "media_posted",
        DISTRICT_POINTS_UPDATED: "district_points_updated",
        SCHEDULE_POSTED: "schedule_posted",
        FINAL_RESULTS: "final_results",
        PING: "ping",
        BROADCAST: "broadcast",

        UPDATE_FAVORITES: "update_favorites",
        UPDATE_SUBSCRIPTION: "update_subscriptions",

        VERIFICATION: "verification"
    }

    render_names = {
        UPCOMING_MATCH: "Upcoming Match",
        MATCH_SCORE: "Match Score",
        LEVEL_STARTING: "Competition Level Starting",
        ALLIANCE_SELECTION: "Alliance Selection",
        AWARDS: "Awards Posted",
        MEDIA_POSTED: "Media Posted",
        DISTRICT_POINTS_UPDATED: "District Points Updated",
        SCHEDULE_POSTED: "Event Schedule Posted",
        FINAL_RESULTS: "Final Results",
    }

    types = {
        "upcoming_match": UPCOMING_MATCH,
        "match_score": MATCH_SCORE,
        "starting_comp_level": LEVEL_STARTING,
        "alliance_selection": ALLIANCE_SELECTION,
        "awards_posted": AWARDS,
        "media_posted": MEDIA_POSTED,
        "district_points_updated": DISTRICT_POINTS_UPDATED,
        "schedule_posted": SCHEDULE_POSTED,
        "final_results": FINAL_RESULTS,

        "update_favorites": UPDATE_FAVORITES,
        "update_subscriptions": UPDATE_SUBSCRIPTION,

        "verification": VERIFICATION
    }

    enabled_notifications = {
        MATCH_SCORE: render_names[MATCH_SCORE]
    }
