# Requirement ID: FR_hybrid_1
- Description: [The system shall allow users to select their preferred narrator to narrate mediation sessions.  ]
- Source Persona: [Satisfied User]
- Traceability: [Derived from review group H1]
- Acceptance Criteria: [Given a user has selected their preferred narrator, when they open a meditation session, Then the system must automatically start playing the session that narrated by the selected narrator.  ]
- Notes: [Automated FR was too vague.  I refined it by focussing in on something that is directly testable.  ]


# Requirement ID: FR_hybrid_2
- Description: [The system shall notify users a week prior to regarding content they consume that's to be pay walled.  ]
- Source Persona: [Satisfied User]
- Traceability: [Derived from review group H1]
- Acceptance Criteria: [Given when a user has previously accessed some content, When it is set to be pay walled, Then the system must send an in-app notification at least a week prior that explicitly states the change.  ]
- Notes: [Had to derive a new FR because the automated spec only had 5 as task 4 step 4.4 did not specifiy as to how many FRs we should have.  Focusses in on content that's actively being consumed abruptly being pay walled.  ]


# Requirement ID: FR_hybrid_3
- Description: [The system shall maintain uninterrupted session audio for a minimum of 8 continuous hours.  ]
- Source Persona: [Poor Sleeper]
- Traceability: [Derived from review group H2]
- Acceptance Criteria: [Given a user starts a sleep session, When 8 hours have passed, Then the application must still be playing the audio without interruption from crahses or unexpected pauses.  ]
- Notes: [Automated FR_auto_2 was refined to be less vague to include a proper testable threshold for playback consistency.  ]


# Requirement ID: FR_hybrid_4
- Description: [The system shall provide a sleep audio library with a large variety of narrator voices and environmental sounds, where both should have at least 10 different options.  ]
- Source Persona: [Poor Sleeper]
- Traceability: [Derived from review group H2]
- Acceptance Criteria: [Given a user navigates to the sleep audio section, When the broswe the available content, Then the system must display sleep stores from at least 10 distinct narrators and environmental sounds.  ]
- Notes: [Had to derive a new FR because the automated spec only had 5 as task 4 step 4.4 did not specifiy as to how many FRs we should have.  Focusses in on variety of narrator voices and nature sounds.  ]


# Requirement ID: FR_hybrid_5
- Description: [The system shall return accurate search results for mediatation content within 2 seconds of a user submitting their input.  ]
- Source Persona: [Mental Wellness Improvement Seeker]
- Traceability: [Derived from review group H3]
- Acceptance Criteria: [Given a user submits a search request in the meditation content search bar, when the request is processed, then the system must display the results within 2 seconds.  ]
- Notes: [Refined FR_auto_3 to replace vague navigation language with a specific and testable search performance requirement.]


# Requirement ID: FR_hybrid_6
- Description: [The system shall ensure the narrator voice remains clearly audible above background audio at all volume settings.  ]
- Source Persona: [Mental Wellness Improvement Seeker]
- Traceability: [Derived from review group H3]
- Acceptance Criteria: [Given a meditation session is playing with background sounds, When the session is in progress, Then the narrator voice must be clearly audible and must not be drowned out by the background audio at any point.  ]
- Notes: [Had to derive a new FR because the automated spec only had 5 as task 4 step 4.4 did not specifiy as to how many FRs we should have.  Focusses in on background and narrator voice balancing.  ]

# Requirement ID: FR_hybrid_7
- Description: [The system shall provide free-tier users access to at least 5 guided meditation sessions and 3 sleep stories without requiring a subscription.  ]
- Source Persona: [Frustrated Free to Use Individual]
- Traceability: [Derived from review group H4]
- Acceptance Criteria: [Given a user is on the free tier model, When they navigate to the meditation or sleep sections, Then the system must grant access to at least 5 guided meditation sessions and 3 sleep stories without prompting a subscription upgrade.  ]
- Notes: [Refined FR_auto_4 to replace vague affordability language with a specific and measurable free content access requirement.  ]


# Requirement ID: FR_hybrid_8
- Description: [The system shall clearly display all free trial details including duration, subscription price, and billing date before a user confirms sign-up.  ]
- Source Persona: [Frustrated Free to Use Individual]
- Traceability: [Derived from review group H4]
- Acceptance Criteria: [Given a user is on the free trial sign-up page, When they reach the payment confirmation step, Then the system must clearly display the trial duration, subscription price post free trial, and exact billing date before the user confirms.  ]
- Notes: [Had to derive a new FR because the automated spec only had 5 as task 4 step 4.4 did not specifiy as to how many FRs we should have.  Focusses in on explicitness of subscription details and conditions.   ]


# Requirement ID: FR_hybrid_9
- Description: [The system shall not charge a user after they have cancelled a free trial or subscription.  ]
- Source Persona: [Wrongfully Charged Subscriber]
- Traceability: [Derived from review group H5]
- Acceptance Criteria: [Given a user has cancelled a free trial or subscription, When the cancellation is confirmed, Then the system must not proceed with any further charges to the user's payment method.  ]
- Notes: [Refined FR_auto_5 to replace vague personalization language with a specific billing protection.  ]


# Requirement ID: FR_hybrid_10
- Description: [The system shall process refund requests for unwanted subscription charges within 3 business days of submission.  ]
- Source Persona: [Wrongfully Charged Subscriber]
- Traceability: [Derived from review group H5]
- Acceptance Criteria: [Given a user submits a refund request for an unwanted/unintended charge, When 3 business days have passed, Then the system must have processed the refund and notified the user of the result via email.  ]
- Notes: [Had to derive a new FR because the automated spec only had 5 as task 4 step 4.4 did not specifiy as to how many FRs we should have.  Focusses in on timely refunds.  ]