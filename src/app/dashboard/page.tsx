'use client';
import React, { ReactElement } from 'react';
import withSession from '@/components/auth-wrapper';
import { RucioUser } from '@/lib/core/entity/auth-models';

const Dashboard = ({ user }: { user: RucioUser }): ReactElement => {
  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome to the dashboard, {user.rucioIdentity}</p>
    </div>
  );
}

export default withSession(Dashboard);
