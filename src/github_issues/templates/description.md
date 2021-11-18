{% if author_name %}Author: {% if author_github_username %}{{ author_github_username }} ({{ author_name }}){% else %}**{{ author_name }}**{% endif %}{% endif %}
{% if start_date %}Date: {{ start_date }}{% endif %}
{% if bugzilla %}Bugzilla: https://bugzilla.redhat.com/buglist.cgi?quicksearch={{bugzilla}}{% endif %}
{% if redmine_link %}Redmine Issue: {{ redmine_issue_num }}, {{redmine_link}}{% endif %}

---

{{ description }}



