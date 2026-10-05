# Take-home: Lead Follow-Up Tool

## Context

You're building a small internal tool for a car dealership's sales team. Salespeople manage
leads (people interested in buying a car) by hand today, in a spreadsheet, and follow-ups fall
through the cracks constantly.

## The ask

Build a small web app that helps a sales team track leads and know which ones need follow-up
before they go cold.

A salesperson seeing the right leads flagged when they open the app counts as "knowing". You
do not need to push anything to them (no email/SMS/Slack required, though you're welcome to if you
want). Use your judgment on what "goes cold" means and what a lead record needs. Write down 
the decisions you made and why.

## Requirements

- See leads and each one's status, add a new lead, update one.
- Something in the system surfaces which leads need follow-up, without a person having to go
  looking for them. This doesn't need to be a running background job, and a view or endpoint that
  computes it is enough. Don't spend your time setting up a scheduler.
- Design the data as if more than one salesperson uses this (a lead belongs to someone). You don't
  need to build login logic or a full multi-user UI. One implicit user is fine. We're looking at
  the data model, not an auth system.

Anything not listed above is your call. If you're unsure whether something is in scope, make a
call and note the assumption rather than asking.

## Stack

This repo is the base you'll build on. It consists of a FastAPI backend wired to a local
SQLite file via SQLAlchemy, and a Vite + React frontend already proxied to it. Nothing
feature-specific is built yet. Follow the main README to get it running, then build on top of it.

- Backend: Python, FastAPI, SQLAlchemy (already wired to SQLite — no separate database setup
  needed)
- Frontend: React, functional is enough — don't spend time on styling
- Both should run locally with the existing setup

## What to submit

- Clone this repo. Then either push your version to a new
  public repo under your own GitHub account and send us the link, or zip up your project folder
  and email it to us.
- A README covering: how to run it, the decisions and assumptions you made, what you'd do next
  with more time, and which AI tools you used and how.

## Time

Aim for 2 hours. This is unpaid, so please don't go past that — a smaller, well-reasoned
submission is worth more to us than a bigger, rushed one.

## What we're looking at

Not polish. We're looking at the decisions you made without being told what to do, whether you
handled the parts of the problem we didn't spell out (what happens with no leads, a bad input, two
salespeople, a job that runs more than once), and whether your write-up explains your thinking
clearly.
