let ctx = document.getElementById('myTuitionChart');
let act = document.getElementById('myActChart');
let sat = document.getElementById('mySatChart');
let admission = document.getElementById('myAdmissionChart');
let demographics = document.getElementById('demographicChart');
let litLanguageSocialScience = document.getElementById('litLanguageSocialScience');
let engineeringAndTechnology = document.getElementById('engineering&Technology');
let business = document.getElementById('business');
let scienceAndMath = document.getElementById('science&Math');
let arts = document.getElementById('arts');
let social = document.getElementById('socialSciences');

let socialSciencesChart = new Chart(social, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Social Science (' + (socialScience * 100).toFixed(2) + '%)',
            data: [(socialScience * 100).toFixed(2)],
             backgroundColor: ['rgba(51, 0, 235, 0.53)']
        },
        {
            label: 'Public Administration (' + (publicAdministration * 100).toFixed(2) + '%)',
            data: [(publicAdministration * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Ethnic Cultural/Gender Studies (' + (ethnicCulturalGender * 100).toFixed(2) + '%)',
            data: [(ethnicCulturalGender * 100).toFixed(2)],
            backgroundColor: ['rgba(117, 11, 11, 0.79)']
        },
        {
            label: 'Psychology (' + (psychology * 100).toFixed(2) + '%)',
            data: [(psychology * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 223, 0, 0.53)']
        },
        {
            label: 'Education (' + (education * 100).toFixed(2) + '%)',
            data: [(education * 100).toFixed(2)],
            backgroundColor: ['rgba(117, 11, 111, 0.79)']
        },
        {
            label: 'Legal (' + (legal * 100).toFixed(2) + '%)',
            data: [(legal * 100).toFixed(2)],
            backgroundColor: ['rgba(166, 149, 17, 0.79)']
        },
        {
            label: 'Humanities (' + (humanities * 100).toFixed(2) + '%)',
            data: [(humanities * 100).toFixed(2)],
            backgroundColor: ['rgba(231, 107, 24, 0.79)']
        },
        {
            label: 'Security & Law Enforcement (' + (securityLawEnforcement * 100).toFixed(2) + '%)',
            data: [(securityLawEnforcement * 100).toFixed(2)],
            backgroundColor: ['rgba(28, 24, 231, 0.79)']
        },
        ]
    },
    options: {
        title: {
          display: true,
          text: 'Social Sciences (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true
            }],
            xAxes: [{
                stacked: true
            }],
        }
    }
});

let artsChart = new Chart(arts, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Architecture (' + (architecture * 100).toFixed(2) + '%)',
            data: [(architecture * 100).toFixed(2)],
             backgroundColor: ['rgba(182, 84, 84, 0.79)']
        },
        {
            label: 'Visual Performing (' + (visualPerforming * 100).toFixed(2) + '%)',
            data: [(visualPerforming * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Personal Culinary (' + (personalCulinary * 100).toFixed(2) + '%)',
            data: [(personalCulinary * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Multi Discipline (' + (multiDiscipline * 100).toFixed(2) + '%)',
            data: [(multiDiscipline * 100).toFixed(2)],
            backgroundColor: ['rgba(27, 17, 166, 0.79)']
        },
        {
            label: 'Military (' + (military * 100).toFixed(2) + '%)',
            data: [(military * 100).toFixed(2)],
            backgroundColor: ['rgba(166, 17, 146, 0.79)']
        },
        {
            label: 'Parks & Recreation & Fitness (' + (parksRecreationFitness * 100).toFixed(2) + '%)',
            data: [(parksRecreationFitness * 100).toFixed(2)],
            backgroundColor: ['rgba(166, 149, 17, 0.79)']
        },
        ]
    },
    options: {
        title: {
          display: true,
          text: 'Arts & Other (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true
            }],
            xAxes: [{
                stacked: true
            }],
        }
    }
});

let scienceAndMathChart = new Chart(scienceAndMath, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Health (' + (health * 100).toFixed(2) + '%)',
            data: [(health * 100).toFixed(2)],
             backgroundColor: ['rgba(182, 84, 84, 0.79)']
        },
        {
            label: 'Mathematics (' + (mathematics * 100).toFixed(2) + '%)',
            data: [(mathematics * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Biology (' + (biological * 100).toFixed(2) + '%)',
            data: [(biological * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Family Consumer Science (' + (familyConsumerScience * 100).toFixed(2) + '%)',
            data: [(familyConsumerScience * 100).toFixed(2)],
            backgroundColor: ['rgba(28, 24, 231, 0.79)']
        },
        {
            label: 'Physical Science (' + (physicalScience * 100).toFixed(2) + '%)',
            data: [(physicalScience * 100).toFixed(2)],
            backgroundColor: ['rgba(0, 235, 51, 0.53)']
        },
        {
            label: 'Agriculture (' + (agriculture * 100).toFixed(2) + '%)',
            data: [(agriculture * 100).toFixed(2)],
            backgroundColor: ['rgba(17, 166, 129, 0.79)']
        },
        ]
    },
    options: {
        title: {
          display: true,
          text: 'Science & Math (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true
            }],
            xAxes: [{
                stacked: true
            }],
        }
    }
});

let businessChart = new Chart(business, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Business Marketing (' + (businessMarketing * 100).toFixed(2) + '%)',
            data: [(businessMarketing * 100).toFixed(2)],
             backgroundColor: ['rgba(90, 182, 84, 0.79)']
        },
        {
            label: 'Resources (' + (resources * 100).toFixed(2) + '%)',
            data: [(resources * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Transportation (' + (transportation * 100).toFixed(2) + '%)',
            data: [(transportation * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Construction Management (' + (construction * 100).toFixed(2) + '%)',
            data: [(construction * 100).toFixed(2)],
            backgroundColor: ['rgba(28, 24, 231, 0.79)']
        },
        ]
    },
    options: {
        title: {
          display: true,
          text: 'Business-Related (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true
            }],
            xAxes: [{
                stacked: true
            }],
        }
    }
});

let engineeringTechChart = new Chart(engineeringAndTechnology, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Engineering (' + (engineering * 100).toFixed(2) + '%)',
            data: [(engineering * 100).toFixed(2)],
             backgroundColor: ['rgba(51, 0, 235, 0.53)']
        },
        {
            label: 'Engineering Technology (' + (engineeringTechnology * 100).toFixed(2) + '%)',
            data: [(engineeringTechnology * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 231, 0.53)']

        },
        {
            label: 'Communications Technology (' + (communicationsTechnology * 100).toFixed(2) + '%)',
            data: [(communicationsTechnology * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Mechanic Repair Technology (' + (mechanicRepairTechnology * 100).toFixed(2) + '%)',
            data: [(mechanicRepairTechnology * 100).toFixed(2)],
            backgroundColor: ['rgba(0, 235, 51, 0.53)']
        },
        {
            label: 'Science Technology (' + (scienceTechnology * 100).toFixed(2) + '%)',
            data: [(scienceTechnology * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 223, 0, 0.53)']
        },
        {
            label: 'Computer Science (' + (computer * 100).toFixed(2) + '%)',
            data: [(computer * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 141, 0, 0.65)']
        },
        {
            label: 'Precision Production (' + (precisionProduction * 100).toFixed(2) + '%)',
            data: [(precisionProduction * 100).toFixed(2)],
            backgroundColor: ['rgba(11, 20, 117, 0.79)']
        },
        ]
    },
    options: {
        title: {
          display: true,
          text: 'Engineering & Technology (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true
            }],
            xAxes: [{
                stacked: true
            }],
        }
    }
});

let litLanguageChart = new Chart(litLanguageSocialScience, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [
        {
            label: 'Religious Philosophy (' + (philosophyReligious * 100).toFixed(2) + '%)',
            data: [(philosophyReligious * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 0, 0, 0.53)']
        },
        {
            label: 'Theology Religious Vocation (' + (theologyReligiousVocation * 100).toFixed(2) + '%)',
            data: [(theologyReligiousVocation * 100).toFixed(2)],
            backgroundColor: ['rgba(0, 235, 51, 0.53)']
        },
        {
            label: 'Library (' + (library * 100).toFixed(2) + '%)',
            data: [(library * 100).toFixed(2)],
            backgroundColor: ['rgba(235, 141, 0, 0.65)']
        },
        {
            label: 'History (' + (history * 100).toFixed(2) + '%)',
            data: [(history * 100).toFixed(2)],
            backgroundColor: ['rgba(11, 20, 117, 0.79)']
        },
        {
            label: 'English (' + (english * 100).toFixed(2) + '%)',
            data: [(english * 100).toFixed(2)],
            backgroundColor: ['rgba(69, 117, 11, 0.79)']
        },
        {
            label: 'Communication (' + (communication * 100).toFixed(2) + '%)',
            data: [(communication * 100).toFixed(2)],
            backgroundColor: ['rgba(11, 117, 110, 0.79)']
        },
        {
            label: 'Language (' + (language * 100).toFixed(2) + '%)',
            data: [(language * 100).toFixed(2)],
            backgroundColor: ['rgba(67, 117, 11, 0.79)']
        },
        ]
    },
    options: {
        title: {
          display: true,
          text: 'Literature & Language (%)'
        },
        legend: {
            display: true
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                stacked: true
            }],
            xAxes: [{
                stacked: true
            }],
        }
    }
});

let demographicChart = new Chart(demographics, {
    type: 'pie',
    data: {
        labels: ['Caucasian (' + (caucasian * 100).toFixed(2) + '%)', 'African American (' + (africanAmerican * 100).toFixed(2) + '%)', 'Hispanic (' + (hispanic * 100).toFixed(2) + '%)', 'Asian (' + (asian * 100).toFixed(2) + '%)',
            'Pacific Islander (' + (pacificIslander * 100).toFixed(2) + '%)', 'Multi-Racial (' + (multiRacial * 100).toFixed(2) + '%)', 'Non-Resident (' + (nonResident * 100).toFixed(2) + '%)',
            'American Indian/Alaskan native (' + (aian * 100).toFixed(2) + '%)'],
        datasets: [{
            label: 'Demographic Percentages (%)',
            data: [(caucasian * 100).toFixed(2), (africanAmerican * 100).toFixed(2),
                (hispanic * 100).toFixed(2), (asian * 100).toFixed(2),
                (pacificIslander * 100).toFixed(2), (multiRacial * 100).toFixed(2),
                (nonResident * 100).toFixed(2), (aian * 100).toFixed(2)],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(176, 85, 90, 0.2)',
                'rgba(120, 45, 200, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(25, 102, 255, 1)',
                'rgba(190, 98, 78, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend : {
            position: 'left',
        },
        title: {
          display: false,
          text: 'Demographic Percentages (%)'
        },
    }
});

let myTuitionChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['In-State Tuition ($' + (parseInt(inStateTuition)).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,') + ')', 'Out-of-State Tuition ($' + (parseInt(outStateTuition)).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,') + ')'],
        datasets: [{
            label: 'Tuition in USD ($)',
            data: [parseInt(inStateTuition), parseInt(outStateTuition)],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        title: {
          display: true,
          text: 'Tuition in USD ($)'
        },
        legend: {
            display: false
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

let myActChart = new Chart(act, {
    type: 'bar',
    data: {
        labels: ['ACT Score (' + parseInt(actScore) + ')'],
        datasets: [{
            label: 'ACT Score (out of 36)',
            data: [parseInt(actScore)],
            backgroundColor: [
                'rgba(255, 206, 86, 0.2)'
            ],
            borderColor: [
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        title: {
          display: true,
          text: 'Average ACT Score (out of 36)'
        },
        legend: {
            display: false
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    max : 40,
                    min : 0
                }
            }]
        }
    }
});

let mySatChart = new Chart(sat, {
    type: 'bar',
    data: {
        labels: ['SAT Score (' + parseInt(satScore) + ')'],
        datasets: [{
            label: 'SAT Score (out of 1600)',
            data: [parseInt(satScore)],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        title: {
          display: true,
          text: 'Average SAT Score (out of 1600)'
        },
        legend: {
            display: false
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    max : 1600,
                    min : 0
                }
            }]
        }
    }
});